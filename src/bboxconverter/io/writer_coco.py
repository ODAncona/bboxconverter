from pathlib import Path
from pandas.core.frame import DataFrame
import json


def to_coco(df_bbox: DataFrame, output_path: "str | Path"):
    """
    This function will take an array of bounding box and write it to a .json file respecting the coco format

    Parameters
    ----------
    df_bbox : DataFrame
        The dataframe containing the bounding box informations
    output_path : str | Path
        The path to the output file.
    """

    # Create images
    images = []
    for i, img in enumerate(df_bbox['file_path'].unique()):
        row = df_bbox[df_bbox['file_path'] == img].iloc[0]
        images.append(
            dict(
                width=int(row['image_width']),
                height=int(row['image_height']),
                id=i,
                file_name=img,
            ))

    # Create categories
    categories = []
    for i, cat in enumerate(df_bbox['class_name'].unique()):
        categories.append(dict(id=i, name=cat))

    # Create annotations
    image_id = {img:i for i, img in enumerate(df_bbox['file_path'].unique())}
    cat_id = {cat['name']:cat['id'] for cat in categories}

    annotations = df_bbox.apply(
        lambda row: {
            'id': row.name,
            'image_id': image_id[row['file_path']],
            'category_id': cat_id[row['class_name']],
            'segmentation': row['segmentation'] if 'segmentation' in df_bbox.columns else [],
            'bbox': [row['x_min'], row['y_min'], row['width'], row['height']],
            'area': row['width'] * row['height'],
            'iscrowd': 0,
            'ignore': 0,
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
