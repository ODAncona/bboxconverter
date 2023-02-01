import bboxtools.core.bbox as BBox


class CWH_BBox(BBox):
    center_x: int = None
    center_y: int = None
    width: int = None
    height: int = None

    def __init__(self,
                 classname,
                 filename,
                 center_x,
                 center_y,
                 width,
                 height,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(classname, filename, confidence, image_width,
                         image_height)
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        pass

    @classmethod
    def from_TLBR(self, bbox) -> None:
        center_x = (bbox.top_left_x + bbox.bottom_right_x) // 2
        center_y = (bbox.top_left_y + bbox.bottom_right_y) // 2
        width = bbox.bottom_right_x - bbox.top_left_x
        height = bbox.top_left_y - bbox.bottom_right_y
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    center_x=center_x,
                    center_y=center_y,
                    width=width,
                    height=height)

    @classmethod
    def from_TLWH(self, bbox) -> None:
        center_x = bbox.top_left_x + bbox.width // 2
        center_y = bbox.top_left_y - bbox.height // 2
        width = bbox.width
        height = bbox.height
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    center_x=center_x,
                    center_y=center_y,
                    width=width,
                    height=height)

    def __str__(self) -> str:
        return "CWH format: " + super().__str__(
        ) + f" {self.center_x} {self.center_y} {self.width} {self.height}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}
