from ..core.bbox_parser import bbox_parser
from pandas import DataFrame
import json
from os import PathLike


def get_bbox_type(df) -> str:
    bbox_types = [('x_center', 'y_center', 'width', 'height'),
                  ('x_max', 'y_max', 'x_min', 'y_min'),
                  ('x_min', 'y_min', 'width', 'height')]
    for bbox_type, cols in enumerate(bbox_types):
        if all(col in df.columns for col in cols):
            return ['cwh', 'tlbr', 'tlwh'][bbox_type]
    return None


def read_manifest(path: str | PathLike, format='auto') -> None:
    '''
    Read bounding boxes from a manifest file using pandas.read_csv.

    Parameters
    ----------
    path : str | os.PathLike
        Path to csv file
    format : str
        Format of the manifest file. Can be one of the following: 'auto', 'coco', 'pascal'
    '''

    # {'source-ref': 's3://crh-labeling/session_cam/img_1674239767.jpg', 'crh-label-test5': {'image_size': [{'width': 9152, 'height': 6944, 'depth': 3}], 'annotations': [{'class_id': 0, 'top': 4943.666666666667, 'left': 8106, 'height': 427, 'width': 376}, {'class_id': 0, 'top': 5343.666666666667, 'left': 8133.666666666667, 'height': 360, 'width': 376.33333333333303}, {'class_id': 0, 'top': 5655.666666666667, 'left': 8204.333333333334, 'height': 368.66666666666663, 'width': 316.66666666666606}, {'class_id': 0, 'top': 4929, 'left': 8372.333333333334, 'height': 385.66666666666674, 'width': 294}, {'class_id': 0, 'top': 5620.333333333333, 'left': 8471.666666666666, 'height': 354.66666666666674, 'width': 240.33333333333394}, {'class_id': 0, 'top': 5502.666666666667, 'left': 8789, 'height': 337.33333333333326, 'width': 213}, {'class_id': 0, 'top': 4885.333333333334, 'left': 8562.333333333334, 'height': 408.6666666666665, 'width': 270.66666666666606}, {'class_id': 0, 'top': 5194, 'left': 8798.333333333334, 'height': 352.33333333333326, 'width': 231}, {'class_id': 0, 'top': 4849.666666666666, 'left': 8769.666666666666, 'height': 390.3333333333335, 'width': 246}, {'class_id': 0, 'top': 5297.666666666667, 'left': 8479, 'height': 331.6666666666665, 'width': 252.33333333333394}, {'class_id': 0, 'top': 5229.5, 'left': 8634.5, 'height': 316, 'width': 209.5}, {'class_id': 0, 'top': 5541, 'left': 8604, 'height': 352.5, 'width': 250}]}, 'crh-label-test5-metadata': {'objects': [{'confidence': 0.64}, {'confidence': 0.66}, {'confidence': 0.58}, {'confidence': 0.67}, {'confidence': 0.65}, {'confidence': 0.56}, {'confidence': 0.64}, {'confidence': 0.62}, {'confidence': 0.49}, {'confidence': 0.62}, {'confidence': 0.6}, {'confidence': 0.66}], 'class-map': {'0': 'disk'}, 'type': 'groundtruth/object-detection', 'human-annotated': 'yes', 'creation-date': '2023-01-21T19:10:24.755887', 'job-name': 'labeling-job/crh-label-test5'}}

    with open(path, 'r') as f:
        data = DataFrame()
        for line in f:
            json_obj = json.loads(line)
            #print(json_obj)

            # Get the image file path
            filepath = json_obj['source-ref']

            # Get the image information
            img = json_obj['crh-label-test5']['image_size'][0]
            image_width, image_height, image_channel = img.values()

            # Get the bboxes mapping of the classes
            class_map = json_obj['crh-label-test5-metadata']['class-map']

            # Get the bboxes annotations
            annotations = json_obj['crh-label-test5']['annotations']

            bboxes = []
            for annotation in annotations:
                class_id, top, left, height, width = annotation.values()
                class_name = class_map[str(class_id)]
                bbox = dict(
                    class_name=class_name,
                    filepath=filepath,
                    x_min=left,
                    y_min=top,
                    width=width,
                    height=height,
                    image_channel=image_channel,
                    image_width=image_width,
                    image_height=image_height,
                )
                bboxes.append(bbox)
            image = DataFrame(bboxes)
            data = data.append(image, ignore_index=True)

    return bbox_parser(data, 'twlh')
