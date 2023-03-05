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

TODO

## From a XML file

TODO
