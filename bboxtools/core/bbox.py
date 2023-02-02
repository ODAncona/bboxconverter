class BBox:
    classname: str = None
    filename: str = None
    confidence: float = None
    image_width: int = None
    image_height: int = None

    def __init__(self,
                 classname,
                 filename,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        self.classname = classname
        self.filename = filename
        if confidence != None:
            self.confidence = confidence
        if image_width != None:
            self.image_width = image_width
        if image_height != None:
            self.image_height = image_height
        pass

    def __str__(self) -> str:
        return f"A {self.classname} detected with {self.confidence} confidence in image {self.filename} of size {self.image_width} x {self.image_height}"

    def __eq__(self, o: object) -> bool:
        return self.classname == o.classname and self.filename == o.filename and self.confidence == o.confidence and self.image_width == o.image_width and self.image_height == o.image_height


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
    
    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.top_left_x == o.top_left_x and self.top_left_y == o.top_left_y and self.width == o.width and self.height == o.height


class TLBR_BBox(BBox):
    top_left_x: int = None
    top_left_y: int = None
    bottom_right_x: int = None
    bottom_right_y: int = None

    def __init__(self,
                 classname,
                 filename,
                 top_left_x,
                 top_left_y,
                 bottom_right_x,
                 bottom_right_y,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(classname, filename, confidence, image_width,
                         image_height)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y
        pass

    @classmethod
    def from_TLWH(self, bbox) -> None:
        top_left_x = bbox.top_left_x
        top_left_y = bbox.top_left_y
        bottom_right_x = bbox.top_left_x + bbox.width
        bottom_right_y = bbox.top_left_y - bbox.height
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    top_left_x=top_left_x,
                    top_left_y=top_left_y,
                    bottom_right_x=bottom_right_x,
                    bottom_right_y=bottom_right_y,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    @classmethod
    def from_CWH(self, bbox) -> None:
        top_left_x = bbox.center_x - bbox.width // 2
        top_left_y = bbox.center_y + bbox.height // 2
        bottom_right_x = bbox.center_x + bbox.width // 2
        bottom_right_y = bbox.center_y - bbox.height // 2
        return self(classname=bbox.classname,
                    filename=bbox.filename,
                    top_left_x=top_left_x,
                    top_left_y=top_left_y,
                    bottom_right_x=bottom_right_x,
                    bottom_right_y=bottom_right_y,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "TLBR format: " + super().__str__(
        ) + f" {self.top_left_x} {self.top_left_y} {self.bottom_right_x} {self.bottom_right_y}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.top_left_x == o.top_left_x and self.top_left_y == o.top_left_y and self.bottom_right_x == o.bottom_right_x and self.bottom_right_y == o.bottom_right_y


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
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

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
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "CWH format: " + super().__str__(
        ) + f" {self.center_x} {self.center_y} {self.width} {self.height}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.center_x == o.center_x and self.center_y == o.center_y and self.width == o.width and self.height == o.height