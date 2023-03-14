from pathlib import Path
from pandas.core.frame import DataFrame
import json


def to_yolo(df_bbox: DataFrame, output_path: "str | Path"):
    """
    This function will take an array of bounding box and write it to a .json file respecting the yolo format

    Parameters
    ----------
    bboxes : DataFrame
        The dataframe containing the bounding box informations
    output_path : str | Path
        The path to the output file
    """
    print('Not implemented yet')
    return

    images = df_bbox.apply(lambda row: {
        'id': row.name,
        'file_name': row['file_path'],
        'width': row['image_width'],
        'height': row['image_height']
    },
                           axis=1).tolist()

    categories = []
    for i, cat in enumerate(df_bbox['class_name'].unique()):
        categories.append(dict(id=i, name=cat))

    annotations = df_bbox.apply(
        lambda row: {
            'id': row.name,
            'image_id': row.name,
            'category_id': row['class_name'],
            'bbox':
            [row['x_center'], row['y_center'], row['width'], row['height']],
            'area': row['width'] * row['height'],
            'iscrowd': 0
        },
        axis=1).tolist()

    yolo_object = {
        'images': images,
        'categories': categories,
        'annotations': annotations
    }
    with open(output_path, 'w') as outputFile:
        json.dump(yolo_object, outputFile)
