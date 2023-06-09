from ..core.bbox_parser import BboxParser
from pathlib import Path
from json import loads
from pandas.core.frame import DataFrame

def read_coco(path: "str | Path")-> BboxParser:
    """
    Read bounding boxes from a coco file.

    Parameters
    ----------
    path : str | Path
        Path to csv file
        
    Returns
    -------
    BboxParser
        BboxParser object containing bounding boxes
    """

    with open(path, 'r') as f:
        data = loads(f.read())
        categories = {cat['id']: cat['name'] for cat in data['categories']}
        images = {img['id']: img for img in data['images']}
        df_bbox = DataFrame(data['annotations'])
        df_bbox['class_name'] = df_bbox['category_id'].map(categories)
        df_bbox['file_path'] = df_bbox['image_id'].map(lambda x: images[x]['file_name'])
        df_bbox['image_width'] = df_bbox['image_id'].map(lambda x: images[x]['width'])
        df_bbox['image_height'] = df_bbox['image_id'].map(lambda x: images[x]['height'])
        df_bbox[['x_min','y_min','width','height']] = DataFrame(df_bbox['bbox'].tolist(), index=df_bbox.index)
        #df_bbox.drop(columns=['category_id', 'image_id','ignore','iscrowd','area','id','bbox'], inplace=True)
        cols_to_drop = ['category_id', 'image_id', 'ignore', 'iscrowd', 'area', 'id', 'bbox']
        df_bbox.drop(columns=[col for col in cols_to_drop if col in df_bbox.columns], inplace=True)


    return BboxParser(df_bbox, 'tlwh')




