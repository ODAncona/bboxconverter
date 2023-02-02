# BBOX Parser

## Introduction

When you work with bounding box you have severals things to consider.

First, the bounding box could be stored in different ways like:

- TLBR (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
- TLWH (top_left_x, top_left_y, width, height)
- CWH (center_x, center_y, width, height)

Which are popular among different popular format like :

- COCO
- Pascal VOC
- YOLO (You Only Look Once)

Furthermore, the bounding box could be stored in different format like:

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

## Defining a bounding box format

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
