from pandas import read_csv as pd_read_csv
from ..core.bbox_parser import BboxParser
from pathlib import Path


def get_bbox_type(df) -> str:
    bbox_types = [('x_center', 'y_center', 'width', 'height'),
                  ('x_max', 'y_max', 'x_min', 'y_min'),
                  ('x_min', 'y_min', 'width', 'height')]
    for bbox_type, cols in enumerate(bbox_types):
        if all(col in df.columns for col in cols):
            return ['cwh', 'tlbr', 'tlwh'][bbox_type]
    return None


def read_csv(path: str | Path, mapping=None, kwargs={}):
    '''
    Read bounding boxes from a csv file using pandas.read_csv.

    Parameters
    ----------
    path : str | os.Path
        Path to csv file
    mapping : dict
        Dictionary to map column names to bboxconverter standard format
    kwargs : dict
        Keyword arguments for pandas.read_csv
    '''
    # Parse data
    df = pd_read_csv(path, **kwargs)

    # Store them into bbox standard format
    if mapping != None:
        reversed_map = {value: key for key, value in mapping.items()}
        df.columns = df.columns.map(reversed_map)

    # Get bbox type
    bbox_type = get_bbox_type(df)

    return BboxParser(df, bbox_type)
