from importlib.metadata import version

from bboxconverter.io.api import (
    # Input (readers)
    read_coco,
    read_csv,
    read_manifest,
    read_pascal_voc,
    read_xml,
)

__version__ = version("bboxconverter")

__doc__ = """
bboxconverter - easily convert bounding boxes in different formats
=====================================================================

Main Features
-------------
Here are just a few of the things that bboxconverter does well:

- Importing PASCAL VOC XML files
- Importing YOLO TXT files
- Importing COCO JSON files
- Importing CSV files
- Importing TXT files
- Exporting PASCAL VOC XML files
- Exporting YOLO TXT files
- Exporting COCO JSON files
- Exporting CSV files

"""
