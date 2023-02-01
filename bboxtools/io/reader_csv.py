import pandas.io.parsers.readers as readers 
from ..core.bbox_parser import bbox_parser


def get_bbox_type(df) -> str:
    bbox_types = [('center_x', 'center_y', 'width', 'height'),
                  ('bottom_right_x', 'bottom_right_y', 'top_left_x',
                   'top_left_y'),
                  ('top_left_x', 'top_left_y', 'width', 'height')]
    for bbox_type, cols in enumerate(bbox_types):
        if all(col in df.columns for col in cols):
            return ['cwh', 'tlbr', 'tlwh'][bbox_type]
    return None


def read_csv(path, mapping=None, kwargs={}):
    # Parse data
    df = readers.read_csv(path, **kwargs)

    # Store them into bbox standard format
    if mapping != None:
        reversed_map = {value: key for key, value in mapping.items()}
        df.columns = df.columns.map(reversed_map)

    # Get bbox type
    bbox_type = get_bbox_type(df)

    return bbox_parser(df, bbox_type)
