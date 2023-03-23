<img src="https://raw.githubusercontent.com/ODAncona/bboxconverter/main/docs/_static/logo.svg" alt="bbox logo" style="display: block; margin-left:auto; margin-right:auto;"></img>

<p align="center">
    <a href="https://pypi.org/project/bboxconverter">
        <img src="https://img.shields.io/pypi/v/bboxconverter?color=blue" alt="Python versions">
    </a>
    <a href="https://pepy.tech/project/bboxconverter">
        <img src="https://pepy.tech/badge/bboxconverter" alt="Total downloads">
    </a>
    <a href="https://pypi.org/project/bboxconverter">
        <img src="https://img.shields.io/pypi/dm/bboxconverter?color=blue" alt="Monthly downloads">
    </a>
    <a href="https://pypi.org/project/bboxconverter">
        <img src="https://img.shields.io/pypi/pyversions/bboxconverter" alt="Python versions">
    </a>
    </br>
    <a href='https://github.com/ODAncona/bboxconverter/'>
        <img src='https://github.com/ODAncona/bboxconverter/actions/workflows/ci.yml/badge.svg'>
    </a>
    <a href='https://bboxconverter.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/bboxconverter/badge/?version=latest' alt='Documentation Status'/>
    </a>
    <a href="https://codecov.io/gh/ODAncona/bboxconverter" > 
        <img src="https://codecov.io/gh/ODAncona/bboxconverter/branch/main/graph/badge.svg?token=BXGO9JZYWM"/> 
    </a>
</p>

# bboxconverter

bboxconverter is a Python library that enables seamless conversion of bounding box formats between various types and file formats. It provides an easy-to-use syntax for reading and exporting bounding box files.

## Introduction

### What is a bounding box?

Bounding boxes are a crucial component of object detection algorithms, which are used to identify and classify objects within an image or video. A bounding box is a rectangle that surrounds an object of interest in the image, and is typically represented by a set of coordinates that define the box's position and size.

<img src="https://raw.githubusercontent.com/ODAncona/bboxconverter/main/docs/_static/bbox.png" alt="Bounding box example" style="display: block; margin-left:auto; margin-right:auto;"></img>

### Various types and format

When you work with bounding box you have severals things to consider.

The bounding box could be stored in **different types** like:

- Top-Left Bottom-Right (TLBR), (x_min, y_min, x_max, y_max)
- Top-Left Width Height (TLWH), (x_min, y_min, width, height)
- Center Width Height (CWH), (x_center, y_center, width, height)

Which are popular among **different formats** like :

- [COCO](<(http://cocodataset.org/)>) (Common Objects in Context)
- [Pascal VOC](<(http://host.robots.ox.ac.uk/pascal/VOC/)>) (Visual Object Classes)
- [YOLO](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/#yolo) (You Only Look Once)

Furthermore, the bounding box could be stored in **different file formats** like:

- csv
- xml
- json
- manifest
- parquet
- pickle

## Installation

```bash
pip install bboxconverter
```

or

```bash
git clone https://github.com/ODAncona/bboxconverter.git
cd bboxconverter
poetry install
```

See the [installation](https://bboxconverter.readthedocs.io/en/latest/guides/installation.html) guide for more informations.

## Usage

The goal of this library is to seamlessly convert bounding box format using easy syntax.

It should be a breeze like...

```python
import bboxconverter as bc

# Input file path
input_path = './examples/example.csv'

# Output file path
output_path = './examples/output/example.json'

# Mapping between the input file and the bboxconverter format
bbox_map = dict(
    class_name='class',
    file_path='name',
    x_min='top_left_x',
    y_min='top_left_y',
    width='w',
    height='h',
    image_width='img_size_x',
    image_height='img_size_y',
)

# Read the input file
parser = bc.read_csv(input_path, mapping=bbox_map)

# Export the file to the desired format
parser.export(output_path=output_path, format='coco')
parser.export(output_path=output_path, format='voc')
parser.export(output_path=output_path, format='yolo')
```

## Documentation

You can find the documention online at [bboxconvert.readthedoc.io](https://bboxconverter.readthedocs.io/en/latest/index.html)

## Changelog

See the [CHANGELOG](https://github.com/ODAncona/bboxconverter/blob/main/CHANGELOG.md) file for details.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](https://github.com/ODAncona/bboxconverter/blob/main/CONTRIBUTING.md) first.

## License

This project is licensed under the GPLV3 License - see the [LICENSE](https://github.com/ODAncona/bboxconverter/blob/main/LICENSE) file for details.

## Acknowledgments

- [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- [COCO](http://cocodataset.org/#home)
- [YOLO](https://pjreddie.com/darknet/yolo/)
- [Albumentation](https://albumentations.ai/)
- [Pyodi](https://github.com/Gradiant/pyodi)
