from pathlib import Path
from pandas.core.frame import DataFrame
import json


def to_coco(df_bbox: DataFrame, output_path: Path):
    '''
    This function will take an array of bounding box and write it to a .json file respecting the coco format

    Parameters
    ----------
    df_bbox : DataFrame
        The dataframe containing the bounding box informations
    output_path : str | Path
        The path to the output file.
    '''

    # Create images
    images = df_bbox.apply(lambda row: {
        'id': row.name,
        'file_name': row['file_path'],
        'width': row['image_width'],
        'height': row['image_height']
    },
                           axis=1).tolist()

    # Create categories
    categories = []
    for i, cat in enumerate(df_bbox['class_name'].unique()):
        categories.append(dict(id=i, name=cat))

    # Create annotations
    annotations = df_bbox.apply(
        lambda row: {
            'id': row.name,
            'image_id': row.name,
            'category_id': row['class_name'],
            'bbox': [row['x_min'], row['y_min'], row['width'], row['height']],
            'area': row['width'] * row['height'],
            'iscrowd': 0
        },
        axis=1).tolist()

    # Create yolo object
    yolo_object = {
        'images': images,
        'categories': categories,
        'annotations': annotations
    }

    # Write to file
    with open(output_path, 'wt', encoding='UTF-8') as outputFile:
        json.dump(yolo_object, outputFile)
