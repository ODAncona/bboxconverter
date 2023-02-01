import bboxtools.core.bbox as BBox

class TLWH_BBox(BBox):
    top_left_x: int = None
    top_left_y: int = None
    width: int = None
    height: int = None

    def __init__(self,
                 classname,
                 filename,
                 top_left_x,
                 top_left_y,
                 width,
                 height,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(classname, filename, confidence, image_width,
                         image_height)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height
        pass

    @classmethod
    def from_TLBR(self, bbox) -> None:
        top_left_x = bbox.top_left_x
        top_left_y = bbox.top_left_y
        width = bbox.bottom_right_x - bbox.top_left_x
        height = bbox.top_left_y - bbox.bottom_right_y
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    top_left_x=top_left_x,
                    top_left_y=top_left_y,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    @classmethod
    def from_CWH(self, bbox) -> None:
        top_left_x = bbox.center_x - bbox.width // 2
        top_left_y = bbox.center_y + bbox.height // 2
        width = bbox.width
        height = bbox.height
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    top_left_x=top_left_x,
                    top_left_y=top_left_y,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "TLWH format: " + super().__str__(
        ) + f" {self.top_left_x} {self.top_left_y} {self.width} {self.height}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

