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
