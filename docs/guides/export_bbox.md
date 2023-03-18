# Exportating bbox

After you ingested your bounding boxes, you might want to export them to a different format. The library provides a set of functions to export your bounding boxes to different formats.

First thing first, you need to parse your bounding boxes. You can find more information about this in the [parsing guide](parse_bbox.md).

```python
import bboxconverter as bc

# Parse your bounding boxes
parser = bc.read_<format>("path_to_your_file")
```

The format can be one of the following:

- `coco` : COCO format
- `csv` : CSV format
- `manifest` : Manifest format
- `xml` : PASCAL VOC format

## To a COCO format

You can export your bounding boxes to a COCO format using the `export` method and specifying the `format` parameter as `coco`.

```python
# Export your bounding boxes to a COCO format
coco = parser.export("output_path", "coco")
```

## To YOLO format

You can export your bounding boxes to a YOLO format using the `export` method and specifying the `format` parameter as `yolo`.

```python
# Export your bounding boxes to a YOLO format
coco = parser.export("output_path", "yolo")
```

## To PASCAL VOC format

You can export your bounding boxes to a PASCAL VOC format using the `export` method and specifying the `format` parameter as `voc`.

```python
# Export your bounding boxes to a PASCAL VOC format
coco = parser.export("output_path", "voc")
```
