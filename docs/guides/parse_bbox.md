# Parsing bbox

The goal is to ingest bounding box data from different sources and convert it to a common format.

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

## From a JSON file

If the json is in the COCO format, you can use the `read_coco` function.

```Python
import bboxconverter as bc

parser = bc.read_coco("./data/patient_50/result.json")

parser.export("./data/patient_50/coco.json", format="coco", split=True)
```

## From a manifest file

```Python
import bboxconverter as bc

# Input file path
input_path2 = '../examples/manifest_export_demo/example.manifest'

# Configuration of the manifest file
config = {
    'labelling-job-name': 'crh-label-test5',
    'labelling-job-metadata': 'crh-label-test5-metadata',
}

# Read the input file
parser = bc.read_manifest(input_path2, configuration=config)
```

## From a parquet file

## From a XML file
