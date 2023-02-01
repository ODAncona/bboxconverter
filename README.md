# BBOX Parser

## Introduction

When you work with bounding box you have severals things to consider. As it is a data file you can store them using :

- csv
- xml
- json
- manifest
- parquet
- pickle

The coordinates could be stored as:

- TLBR (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
- TLWH (top_left_x, top_left_y, width, height)
- CWH (center_x, center_y, width, height)

which are popular among different format like :

- coco
- pascal_voc
- yolo

## Goal

The goal of this library is to seamlessly convert bounding box format using easy syntax.

It should be a breeze like

```python
import bbox_parser as bbp

bbox = bbp.read_csv(path='./path_to_bbox.csv')

bbox.export(format='coco', output_path='./path_to_bbox_coco.json')
bbox.export(format='voc', output_path='./path_to_bbox_coco.xml')
bbox.export(format='manifest', output_path='./path_to_bbox_coco.manifest')
```

## Defining a bounding box format

A bounding box should have the following attributes:

**Mandatory**

- classname
- filename

**Format Specific**

| TLBR | CWH | TLWH |
| ---- | :-: | ---- |
| <ul><li>top_left_x</li><li>top_left_y</li><li>bottom_right_x</li><li>bottom_right_y</li></ul> | <ul><li>center_x</li><li>center_y</li><li>width</li><li>height</li></ul> | <ul><li>top_left_x</li><li>top_left_y</li><li>width</li><li>height</li></ul> |

**Optional**

- confidence
- image_height
- image_width

Therefore, if you want to specify your own format to the parser you can do it the following way:

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

bbox = bbp.read_csv('./examples/example1.csv', bbox_map)
```
