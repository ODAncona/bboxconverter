# Tutorial: Preparing a dataset for training

In this tutorial, we will go through the steps of preparing a dataset for training. We will use the cats and dogs custom dataset that we created in the previous tutorial.

## Preparing a COCO dataset

In this example, we will prepare a `COCO` dataset using `bboxconverter` package.

We have the following files and folders:

* `images` folder containing images of cats and dogs
* `cat_dog.csv` file containing bounding boxes in `tlwh` format

We will convert the `cat_dog.csv` file to `COCO` format and save it in `coco.json` file.
Furthermore, we will also split the dataset into train and validation sets including the images as well.

First things first, lets import the `bboxconverter` package.

```python
import bboxconverter as bc
```

Then, we will define the input and output file paths. It should point to the input `csv` file to the output `.hson` output file respectively.

```python
# Input file path
input_path2 = './examples/csv_prepare_coco_dataset/cat_dog.csv'

# Output file path
output_coco = './examples/csv_prepare_coco_dataset/coco.json'
```

After, we will define the mapping between the input file and the `bboxconverter` format. The `bboxconverter` package uses some fixed names for the columns in the input file. The keys can be found in the [reference of bbox](../api_reference/bbox.md).

```python
# Mapping between the input file and the bboxconverter format
bbox_map = dict(
    class_name='rectanglelabels',
    file_path='file_name',
    x_min='x',
    y_min='y',
    width='width',
    height='height',
    image_width='original_width',
    image_height='original_height',
)
```

Finally, we will read the input file and export it to the desired format. We will also split the dataset into train and validation sets. The `split` parameters can be specified as `bboxconverter` use the `train_test_split` function from `scikit-learn` package.

```python
# Read the input file
parser = bc.read_csv(input_path2, mapping=bbox_map)

# Export the file to the desired format
parser.export(output_path=output_coco, format='coco', split=True)
```

You have successfully prepared a `COCO` dataset. To inspect the resulting bounding boxes we'll display them in the next section.

## Displaying bounding boxes

In this section we will display bounding boxes on images using `pycocotools` package.

```python
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from pycocotools.coco import COCO

# Load COCO annotations
workdir = './examples/csv_prepare_coco_dataset/train'
annFile = f'{workdir}/coco.json'
coco = COCO(annFile)
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
print(f'COCO categories: \n{" ".join(nms)}\n')

# Get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['cat', 'dog'])
imgIds = coco.getImgIds(catIds=catIds)
img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]

# Load and display image
I = io.imread(
    f'{workdir}/{img["file_name"]}'
)
plt.imshow(I)
plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
coco.showAnns(anns, draw_bbox=True)
```