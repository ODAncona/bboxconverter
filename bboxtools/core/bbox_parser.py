from pandas.core.frame import DataFrame
from bboxtools.core.bbox import BBox, TLBR_BBox, TLWH_BBox, CWH_BBox

FORMAT = ['voc', 'coco', 'yolo']

class bbox_parser():

    data: DataFrame = None
    bbox_type: str = None

    def __init__(self, data : DataFrame, bbox_type) -> None:
        self.data = data
        self.bbox_type = bbox_type
        pass

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

        # Conversion function map (output_format, input_bbox_type)
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

        out = DataFrame.from_dict(bboxes.to_list())
        out.to_csv(output_path, index=False)

    def __str__(self) -> str:
        return self.data.to_string()
