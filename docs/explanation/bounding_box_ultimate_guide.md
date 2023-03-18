# Bounding box Ultimate Guide

## What is a bounding box ?

Bounding boxes are a crucial component of object detection algorithms, which are used to identify and classify objects within an image or video. A bounding box is a rectangle that surrounds an object of interest in the image, and is typically represented by a set of coordinates that define the box's position and size. These boxes can be used to locate and extract objects from an image, and can also provide important information about the size, shape, and orientation of the objects

## Bounding box types

### Top-Left Bottom-Right (TLBR)

This format is used to represent a bounding box with four values in pixels: `[x_min, y_min, x_max, y_max]`. `x_min` and `y_min` are coordinates of the top-left corner of the bounding box. `x_max` and `y_max` are coordinates of bottom-right corner of the bounding box.

### Top-Left Width Height (TLWH)

This format is used to represent a bounding box with four values in pixels: `[x_min, y_min, width, height]`. They are coordinates of the top-left corner along with the width and height of the bounding box.

### Center Width Height (CWH)

This format is used to represent a bounding box with four values in pixels: `[x_center, y_center, width, height]`. `x_center` and `y_center` are the coordinates of the center of the bounding box. The `width` and `height` are the length of the bounding box.

## Bounding box format

### Pascal_VOC (TLBR, xml)

`pascal_voc` is a format used by the [Pascal VOC dataset](http://host.robots.ox.ac.uk/pascal/VOC/). coordinates of a bounding box are encoded with four values in pixels: `[x_min, y_min, x_max, y_max]`. `x_min` and `y_min` are coordinates of the top-left corner of the bounding box. `x_max` and `y_max` are coordinates of bottom-right corner of the bounding box.

### COCO (TLWH, json)

coco is a format used by the [Common Objects in Context COCO](http://cocodataset.org/) dataset.

In coco, a bounding box is defined by four values in pixels `[x_min, y_min, width, height]`. They are coordinates of the top-left corner along with the width and height of the bounding box.

### YOLO (CWH, txt)

In yolo, a bounding box is represented by four values `[x_center , y_center, width, height]`. `x_center` and `y_center` are the normalized coordinates of the center of the bounding box. The `width` and `height` are the normalized length. To convert YOLO in other format it is important to have the size of the image to calculate the normalization.
To normalize coordinates, we take pixel values of x and y, which marks the center of the bounding box on the x- and y-axis. Then we divide the value of x by the width of the image and value of y by the height of the image.

### Augmented Manifest Image Format (TLWH, manifest)

Object bounding Box JSON lines is a format used by the [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html) suite. The format is documented in the [Amazon SageMaker documentation](https://sagemaker-examples.readthedocs.io/en/latest/ground_truth_labeling_jobs/object_detection_augmented_manifest_training/object_detection_augmented_manifest_training.html).

### Albumentation (TLBR)

Albumentations is similar to pascal_voc, because it also uses four values `[x_min, y_min, x_max, y_max]` to represent a bounding box. But unlike pascal_voc, albumentations uses normalized values. To normalize values, we divide coordinates in pixels for the x- and y-axis by the width and the height of the image.

Albumentation is a library for image augmentation. It is used in the [albumentations](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/) bounding box augmentation documentation.
