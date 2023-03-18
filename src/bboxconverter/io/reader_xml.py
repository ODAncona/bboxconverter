from ..core.bbox_parser import BboxParser
import xml.etree.ElementTree as ET
from pathlib import Path


def read_xml(path: "str | Path") -> BboxParser:
    """
    Reads bounding boxes from an xml file and returns a BboxParser object.

    Parameters
    ----------
    path : str | Path
        Path to the xml folder.

    Returns
    -------
    BboxParser
        BboxParser object containing bounding boxes
    """
    # parse xml file
    print("Not Implemented")
    pass
