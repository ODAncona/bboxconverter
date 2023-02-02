# BBOX Parser

## Introduction

When you work with bounding box you have severals things to consider.

First, the bounding box could be stored in different ways like:

- TLBR (x_min, y_min, x_max, y_max)
- TLWH (x_min, y_min, width, height)
- CWH (x_center, y_center, width, height)

Which are popular among different popular formats like :

- COCO (Common Objects in Context)
- Pascal_voc (Visual Object Classes)
- YOLO (You Only Look Once)
- Albumentation

Furthermore, the bounding box could be stored in different file formats like:

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
    top_left_x='x',
    top_left_y='y',
    width='w',
    height='h',
    image_width='img_width',
    image_height='img_height',
)

# Read the file and export it to a new format
bbox_parser = bt.read_csv(input_path, mapping=bbox_map)
bbox_parser.export(output_path=output_path, format='yolo')
```

## Bounding box format

### Popular format

#### pascal_voc (TLBR)

`pascal_voc` is a format used by the [Pascal VOC dataset](http://host.robots.ox.ac.uk/pascal/VOC/). coordinates of a bounding box are encoded with four values in pixels: `[x_min, y_min, x_max, y_max]`. `x_min` and `y_min` are coordinates of the top-left corner of the bounding box. `x_max` and `y_max` are coordinates of bottom-right corner of the bounding box.

#### coco (TLWH)

coco is a format used by the [Common Objects in Context COCO](http://cocodataset.org/) dataset.

In coco, a bounding box is defined by four values in pixels `[x_min, y_min, width, height]`. They are coordinates of the top-left corner along with the width and height of the bounding box.

#### yolo (CWH)

In yolo, a bounding box is represented by four values `[x_center , y_center, width, height]`. `x_center` and `y_center` are the normalized coordinates of the center of the bounding box. The `width` and `height` are the normalized length. To convert YOLO in other format it is important to have the size of the image to calculate the normalization.
To normalize coordinates, we take pixel values of x and y, which marks the center of the bounding box on the x- and y-axis. Then we divide the value of x by the width of the image and value of y by the height of the image.

#### albumentation (TLBR)

Albumentations is similar to pascal_voc, because it also uses four values `[x_min, y_min, x_max, y_max]` to represent a bounding box. But unlike pascal_voc, albumentations uses normalized values. To normalize values, we divide coordinates in pixels for the x- and y-axis by the width and the height of the image.

Albumentation is a framework for image augmentation. It is used in the [Albumentations](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/).

### Generic format

A bounding box should have the following attributes:

**Mandatory**

- classname
- filename

**Format Specific**

| TLBR                                                                                          |                                   CWH                                    | TLWH                                                                         |
| --------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------: | ---------------------------------------------------------------------------- |
| <ul><li>top_left_x</li><li>top_left_y</li><li>bottom_right_x</li><li>bottom_right_y</li></ul> | <ul><li>center_x</li><li>center_y</li><li>width</li><li>height</li></ul> | <ul><li>top_left_x</li><li>top_left_y</li><li>width</li><li>height</li></ul> |

**Optional**

- confidence
- image_height
- image_width

Therefore, if you want to specify your own format to the parser you can do it with a mapping like the example below:

If your CSV header looks like:

`class, top, left, w, h, img_size_x, img_size_y, filename`

You could prepare a mapping for the parser like this:

```Python

bbox_map = dict(
    classname='class',
    filename='filename',
    top_left_x='left',
    top_left_y='top',
    width='w',
    height='h',
    image_width='img_size_x',
    image_height='img_size_y',
)

bbox_parser = bt.read_csv('./file.json', bbox_map)
```
