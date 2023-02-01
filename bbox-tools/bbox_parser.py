import pandas as pd
import json

# Bounding Box Library
from bbox import (BBox, TLBR_BBox, TLWH_BBox, CWH_BBox)

FORMAT = ['voc', 'coco', 'yolo']


class bbox_parser():

    data: pd.DataFrame = None
    bbox_type: str = None

    def __init__(self) -> None:
        self.data = pd.DataFrame()
        pass

    def read_manifest(self, path, format='auto') -> None:
        print("Not Implemented")
        with open(path, 'r') as f:
            for line in f:
                json_obj = json.loads(line)
                print(json_obj)
                print("\n")
        pass

    def read_csv(self, path, mapping=None, kwargs={}) -> None:
        # Parse data
        self.data = pd.read_csv(path, **kwargs)

        # Store them into bbox standard format
        if mapping != None:
            reversed_map = {value: key for key, value in mapping.items()}
            self.data.columns = self.data.columns.map(reversed_map)

        # Get bbox type
        self.bbox_type = self.get_bbox_type()

    def read_xml(self, path, mapping=None, kwargs={}) -> None:
        print("Not Implemented")
        pass

    def get_bbox_type(self) -> str:
        bbox_types = [('center_x', 'center_y', 'width', 'height'),
                      ('bottom_right_x', 'bottom_right_y', 'top_left_x',
                       'top_left_y'),
                      ('top_left_x', 'top_left_y', 'width', 'height')]
        for bbox_type, cols in enumerate(bbox_types):
            if all(col in self.data.columns for col in cols):
                return ['cwh', 'tlbr', 'tlwh'][bbox_type]
        return None

    def create_bbox(self, bbox_type: str, **kwargs) -> BBox:
        if bbox_type == 'tlbr':
            return TLBR_BBox(**kwargs)
        if bbox_type == 'tlwh':
            return TLWH_BBox(**kwargs)
        if bbox_type == 'cwh':
            return CWH_BBox(**kwargs)
        return None

    def export(self, output_path, format: str) -> None:
        assert self.bbox_type is not None

        format_map = {
            ('voc', 'tlwh'): TLBR_BBox.from_TLWH,
            ('voc', 'cwh'): TLBR_BBox.from_CWH,
            ('voc', 'tlbr'): True,
            ('coco', 'tlbr'): TLWH_BBox.from_TLBR,
            ('coco', 'cwh'): TLWH_BBox.from_CWH,
            ('coco', 'tlwh'): True,
            ('yolo', 'tlbr'): CWH_BBox.from_TLBR,
            ('yolo', 'tlwh'): CWH_BBox.from_TLWH,
            ('yolo', 'cwh'): True,
        }

        convert_func = format_map.get((format.lower(), self.bbox_type))

        if convert_func is None:
            raise ValueError(
                f"Invalid format: {format} for bbox_type: {self.bbox_type}")

        bboxes = self.data.apply(
            lambda x: self.create_bbox(self.bbox_type, **x.to_dict()), axis=1)
        bboxes = bboxes.apply(lambda x: convert_func(x).to_dict()
                              if convert_func != True else x.to_dict())

        out = pd.DataFrame.from_dict(bboxes.to_list())
        out.to_csv(output_path, index=False)

    def __str__(self) -> str:
        return self.data.to_string()
