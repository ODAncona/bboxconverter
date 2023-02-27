from os import PathLike
import json

def to_yolo(bboxes, output_path):
    '''
    This function will take an array of bounding box and write it to a .json file respecting the yolo format

    Parameters
    ----------
    bboxes : numpy.ndarray
        An array of bounding box
    output_path : str | PathLike
        The path to the output file
    '''

    images = []

    categories = bboxes.categories

    with open(output_path, 'w') as outputFile:
        json.dump(bboxes.tolist(), outputFile)
    