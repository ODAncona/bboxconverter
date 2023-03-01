# bboxtools

## Installation

```bash
git clone https://github.com/ODAncona/bbox-tools.git
cd bbox-tools
python3 setup.py install
```

See the [installation](./documentation/how_to_guide/installation.md) guide for more information.

## Introduction

### What is a bounding box?

Bounding boxes are a crucial component of object detection algorithms, which are used to identify and classify objects within an image or video. A bounding box is a rectangle that surrounds an object of interest in the image, and is typically represented by a set of coordinates that define the box's position and size. These boxes can be used to locate and extract objects from an image, and can also provide important information about the size, shape, and orientation of the objects

### Various types and format

When you work with bounding box you have severals things to consider.

First, the bounding box could be stored in **different types** like:

- Top-Left Bottom-Right(TLBR), (x_min, y_min, x_max, y_max)
- Top-Left Width Height(TLWH), (x_min, y_min, width, height)
- Center Width Height(CWH), (x_center, y_center, width, height)

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
import bboxtools as bt

# Define path to files
input_path = './examples/example1.csv'
output_path = './examples/output/test1.csv'

# Define the header of the raw data
bbox_map = dict(
    classname='class',
    filename='filename',
    x_min='x',
    y_min='y',
    width='w',
    height='h',
    image_width='img_width',
    image_height='img_height',
)

# Read the file and export it to a new format
bbox_parser = bt.read_csv(input_path, mapping=bbox_map)
bbox_parser.export(output_path=output_path, format='yolo')
```

## Documentation

### API Reference

- [BBox](./documentation/api_reference/bbox.md)

### How to guide

- [Installation](./documentation/how_to_guide/installation.md)
- [Parse bbox](./documentation/how_to_guide/parse_bbox.md)
- [Export bbox](./documentation/how_to_guide/export_bbox.md)

### Tutorials

- [Prepare dataset](./documentation/tutorials/prepare_dataset.md)

### Explanation

- [Object detection and bbox](./documentation/explanation/object_detection_and_bbox.md)

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details

## Acknowledgments

- [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- [COCO](http://cocodataset.org/#home)
- [YOLO](https://pjreddie.com/darknet/yolo/)
- [Albumentation](https://albumentations.ai/)
