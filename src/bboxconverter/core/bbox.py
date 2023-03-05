class BBox:
    class_name: str = None
    file_path: str = None
    confidence: float = None
    image_width: int = None
    image_height: int = None

    def __init__(self,
                 class_name,
                 file_path,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        self.class_name = class_name
        self.file_path = file_path
        if confidence != None:
            self.confidence = confidence
        if image_width != None:
            self.image_width = image_width
        if image_height != None:
            self.image_height = image_height
        pass

    def __str__(self) -> str:
        return f"A {self.class_name} detected with {self.confidence} confidence in image {self.file_path} of size {self.image_width} x {self.image_height}"

    def __eq__(self, o: object) -> bool:
        return self.class_name == o.class_name and self.file_path == o.file_path and self.confidence == o.confidence and self.image_width == o.image_width and self.image_height == o.image_height


class TLWH_BBox(BBox):
    x_min: int = None
    y_min: int = None
    width: int = None
    height: int = None

    def __init__(self,
                 class_name,
                 file_path,
                 x_min,
                 y_min,
                 width,
                 height,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(class_name, file_path, confidence, image_width,
                         image_height)
        self.x_min = x_min
        self.y_min = y_min
        self.width = width
        self.height = height
        pass

    @classmethod
    def from_TLBR(self, bbox) -> None:
        x_min = bbox.x_min
        y_min = bbox.y_min
        width = bbox.x_max - bbox.x_min
        height = bbox.y_max - bbox.y_min
        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_min=x_min,
                    y_min=y_min,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    @classmethod
    def from_CWH(self, bbox) -> None:
        width = bbox.width * bbox.image_width
        height = bbox.height * bbox.image_height
        x_min = ((2 * bbox.x_center * bbox.image_width) - width) / 2
        y_min = ((2 * bbox.y_center * bbox.image_height) - height) / 2

        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_min=x_min,
                    y_min=y_min,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "TLWH format: " + super().__str__(
        ) + f" {self.x_min} {self.y_min} {self.width} {self.height}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.x_min == o.x_min and self.y_min == o.y_min and self.width == o.width and self.height == o.height


class TLBR_BBox(BBox):
    x_min: int = None
    y_min: int = None
    x_max: int = None
    y_max: int = None

    def __init__(self,
                 class_name,
                 file_path,
                 x_min,
                 y_min,
                 x_max,
                 y_max,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(class_name, file_path, confidence, image_width,
                         image_height)
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        pass

    @classmethod
    def from_TLWH(self, bbox) -> None:
        x_min = bbox.x_min
        y_min = bbox.y_min
        x_max = bbox.x_min + bbox.width
        y_max = bbox.y_min + bbox.height
        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_min=x_min,
                    y_min=y_min,
                    x_max=x_max,
                    y_max=y_max,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    @classmethod
    def from_CWH(self, bbox) -> None:
        w = bbox.width * bbox.image_width
        h = bbox.height * bbox.image_height
        x_min = ((2 * bbox.x_center * bbox.image_width) - w) / 2
        y_min = ((2 * bbox.y_center * bbox.image_height) - h) / 2
        x_max = x_min + w
        y_max = y_min + h
        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_min=x_min,
                    y_min=y_min,
                    x_max=x_max,
                    y_max=y_max,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "TLBR format: " + super().__str__(
        ) + f" {self.x_min} {self.y_min} {self.x_max} {self.y_max}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.x_min == o.x_min and self.y_min == o.y_min and self.x_max == o.x_max and self.y_max == o.y_max


class CWH_BBox(BBox):
    x_center: int = None
    y_center: int = None
    width: int = None
    height: int = None

    def __init__(self,
                 class_name,
                 file_path,
                 x_center,
                 y_center,
                 width,
                 height,
                 confidence=None,
                 image_width=None,
                 image_height=None) -> None:
        super().__init__(class_name, file_path, confidence, image_width,
                         image_height)
        self.x_center = x_center
        self.y_center = y_center
        self.width = width
        self.height = height
        pass

    @classmethod
    def from_TLBR(self, bbox) -> None:
        x_center = (bbox.x_min + bbox.x_max) / (2 * bbox.image_width)
        y_center = (bbox.y_min + bbox.y_max) / (2 * bbox.image_height)
        width = (bbox.x_max - bbox.x_min) / bbox.image_width
        height = (bbox.y_max - bbox.y_min) / bbox.image_height
        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_center=x_center,
                    y_center=y_center,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    @classmethod
    def from_TLWH(self, bbox) -> None:
        x_center = (2*bbox.x_min + bbox.width) / (2*bbox.image_width)
        y_center = (2*bbox.y_min + bbox.height) / (2*bbox.image_height)
        width = bbox.width / bbox.image_width
        height = bbox.height / bbox.image_height
        return self(class_name=bbox.class_name,
                    file_path=bbox.file_path,
                    x_center=x_center,
                    y_center=y_center,
                    width=width,
                    height=height,
                    confidence=bbox.confidence,
                    image_width=bbox.image_width,
                    image_height=bbox.image_height)

    def __str__(self) -> str:
        return "CWH format: " + super().__str__(
        ) + f" {self.x_center} {self.y_center} {self.width} {self.height}"

    def to_dict(self) -> dict:
        return {k: v for k, v in vars(self).items() if v is not None}

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.x_center == o.x_center and self.y_center == o.y_center and self.width == o.width and self.height == o.height
