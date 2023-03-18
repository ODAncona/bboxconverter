"""
This module imports all the input / output functions for the bboxconverter package who could be used by the user.
"""
from bboxconverter.io.reader_coco import read_coco
from bboxconverter.io.reader_csv import read_csv
from bboxconverter.io.reader_manifest import read_manifest
from bboxconverter.io.reader_pascal_voc import read_pascal_voc
from bboxconverter.io.reader_xml import read_xml
from bboxconverter.io.writer_coco import to_coco
from bboxconverter.io.writer_pascal_voc import to_pascal_voc
from bboxconverter.io.writer_yolo import to_yolo


__all__ = [
    # Input (readers)
    "read_coco",
    "read_csv",
    "read_manifest",
    "read_pascal_voc",
    "read_xml",
    # Output (writers)
    "to_coco",
    "to_pascal_voc"
    "to_yolo",
]
