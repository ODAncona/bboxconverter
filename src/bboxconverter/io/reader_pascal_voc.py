from ..core.bbox_parser import BboxParser
from pathlib import Path
import xml.etree.ElementTree as ET
from pandas.core.frame import DataFrame


def read_pascal_voc(path: "str | Path") -> BboxParser:
    """
    Reads bounding boxes from a pascal_voc folder and returns a BboxParser object.

    Parameters
    ----------
    path : str | Path
        Path to the pascal_voc folder. The folder should contain the following folders:
        - Annotations : contains the xml files
        - Images : contains the images 

    Returns
    -------
    BboxParser
        BboxParser object containing bounding boxes
    """
    annotation_path = Path(path) / "Annotations"
    image_path = Path(path) / "Images"
    xml_files = [x for x in annotation_path.iterdir() if x.suffix == ".xml"]

    bboxes = []
    for annotation in xml_files:
        bboxes.extend(read_content(annotation))

    df_bbox = DataFrame.from_dict(bboxes)

    return BboxParser(df_bbox, 'tlbr')



def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    bboxes = []

    image_width = int(root.find('size/width').text)
    image_height = int(root.find('size/height').text)
    image_channels = int(root.find('size/depth').text)

    for boxes in root.iter('object'):

        filename = root.find('filename').text

        y_min, x_min, y_max, x_max = None, None, None, None

        y_min = int(boxes.find("bndbox/ymin").text)
        x_min = int(boxes.find("bndbox/xmin").text)
        y_max = int(boxes.find("bndbox/ymax").text)
        x_max = int(boxes.find("bndbox/xmax").text)

        bboxes.append(
            dict(
                class_name=boxes.find("name").text,
                file_path=  str(Path(xml_file).parent.parent) + '/images/' + filename,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                image_width=image_width,
                image_height=image_height,
                image_channel=image_channels,
            )
        )
        
    return bboxes