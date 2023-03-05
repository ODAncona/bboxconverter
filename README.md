# bboxconverter

## Installation

```bash
git clone https://github.com/ODAncona/bboxconverter.git
cd bboxconverter
poetry install
```
or

```bash
pip install bboxconverter
```

See the [installation](https://github.com/ODAncona/bbox-tools/blob/main/docs/how_to_guide/installation.md) guide for more information.

## Introduction

### What is a bounding box?

Bounding boxes are a crucial component of object detection algorithms, which are used to identify and classify objects within an image or video. A bounding box is a rectangle that surrounds an object of interest in the image, and is typically represented by a set of coordinates that define the box's position and size. These boxes can be used to locate and extract objects from an image, and can also provide important information about the size, shape, and orientation of the objects

### Various types and format

When you work with bounding box you have severals things to consider.

First, the bounding box could be stored in **different types** like:

- Top-Left Bottom-Right (TLBR), (x_min, y_min, x_max, y_max)
- Top-Left Width Height (TLWH), (x_min, y_min, width, height)
- Center Width Height (CWH), (x_center, y_center, width, height)

Which are popular among **different formats** like :

- COCO (Common Objects in Context)
- Pascal_voc (Visual Object Classes)
- YOLO (You Only Look Once)

Furthermore, the bounding box could be stored in **different file formats** like:

- csv
- xml
- json
- manifest
- parquet
- pickle

## Goal

The goal of this library is to seamlessly convert bounding box format using easy syntax.

It should be a breeze like...

```python
import bboxconverter as bt

# Input file path
input_path1 = './examples/example1.csv'

# Output file path
output_path2 = './examples/output/test2.json'

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
parser = bt.read_csv(input_path1, mapping=bbox_map)

# Export the file to the desired format
parser.export(output_path=output_path2, format='coco')

```

## Documentation

### API Reference

- [BBox](https://github.com/ODAncona/bbox-tools/blob/main/docs/api_reference/bbox.md)

### How to guide

- [Installation](https://github.com/ODAncona/bbox-tools/blob/main/docs/how_to_guide/installation.md)
- [Parse bbox](https://github.com/ODAncona/bbox-tools/blob/main/docs/how_to_guide/parse_bbox.md)
- [Export bbox](https://github.com/ODAncona/bbox-tools/blob/main/docs/how_to_guide/export_bbox.md)

### Tutorials

- [Prepare dataset](https://github.com/ODAncona/bbox-tools/blob/main/docs/tutorials/prepare_dataset.md)

### Explanation

- [Object detection and bbox](https://github.com/ODAncona/bbox-tools/blob/main/docs/explanation/object_detection_and_bbox.md)

## Contributing

Contributions are welcome!

## License

This project is licensed under the GPLV3 License - see the [LICENSE](https://github.com/ODAncona/bbox-tools/blob/main/LICENSE) file for details.

## Acknowledgments

- [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- [COCO](http://cocodataset.org/#home)
- [YOLO](https://pjreddie.com/darknet/yolo/)
- [Albumentation](https://albumentations.ai/)
