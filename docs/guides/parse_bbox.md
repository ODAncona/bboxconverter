# Parsing bbox

The goal is to ingest bounding box data from different sources and convert it to a common format. It could be confusing to deal with different formats and syntaxes. This library aims to provide a common interface to deal with bounding boxes.

The bounding boxes can be stored in popular format like:

- COCO
- YOLO
- PASCAL VOC
- Augmented Manifest

Or they can be stored in a custom format like:

- CSV
- JSON
- Parquet
- XML
- Pickle

## From COCO folder

If you have a coco folder, you can use the `read_coco` function and specify the path of the folder.

```Python
import bboxconverter as bc

parser = bc.read_coco("./data/patient_50")

parser.export("./data/patient_50/coco.json", format="coco", split=True)
```

## From a PASCAL VOC folder

When you have a PASCAL VOC folder, you can use the `read_pascal_voc` function and specify the path of the folder.

```Python
import bboxconverter as bc

parser = bc.read_pascal_voc("./data/patient_50")
```

## From a YOLO folder

When you have a YOLO folder, you can use the `read_yolo` function and specify the path of the folder.

```Python
import bboxconverter as bc

parser = bc.read_yolo("./data/patient_50")
```

## From a CSV file

Let's say you have a CSV file containing your bounding boxes with the following structure:

`class, top, left, w, h, img_size_x, img_size_y, filename`

You will use the `read_csv` function to parse the file and use a mapping to specify the format of the CSV file.

```Python
bbox_map = dict(
    class_name='class',
    file_path='filename',
    x_min='left',
    y_min='top',
    width='w',
    height='h',
    image_width='img_size_x',
    image_height='img_size_y',
)

bbox_parser = bt.read_csv('./file.json', bbox_map)
```

## From an augmented manifest file

If you have some bounding boxes coming from amazon mechanical turk, you can use the `read_manifest` function to parse the file.

```Python
import bboxconverter as bc

# Input file path
input_path2 = '../examples/manifest_export_demo/example.manifest'

# Configuration of the manifest file
config = {
    'labelling-job-name': 'job-name',
    'labelling-job-metadata': 'job-name-metadata',
}

# Read the input file
parser = bc.read_manifest(input_path2, configuration=config)
```

## From a JSON file

TODO

## From a parquet file

TODO

## From a XML file

TODO
