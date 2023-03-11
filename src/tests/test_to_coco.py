import pytest
import bboxconverter as bc
from pathlib import Path
import json
import pandas as pd


@pytest.fixture
def export_csv_to_coco():
    input_path = Path("src/tests/test_data/cat_dog.csv")
    output_path = Path("src/tests/test_data/cat_dog.json")
    bbox_map = dict(
        file_path='file_name',
        class_name='rectanglelabels',
        x_min='x',
        y_min='y',
        width='width',
        height='height',
        image_width='original_width',
        image_height='original_height',
    )
    parser = bc.read_csv(input_path, mapping=bbox_map)
    parser.export(output_path, format="coco")
    yield output_path
    output_path.unlink()


@pytest.fixture
def parsed_coco_output(export_csv_to_coco):
    with open(export_csv_to_coco, "r") as f:
        data = json.load(f)
        anns = pd.json_normalize(data["annotations"])
        imgs = pd.json_normalize(data['images'])
        cats = pd.json_normalize(data['categories'])
        return anns, imgs, cats


class TestClass():

    def test_same_number_of_annotations_and_images(self, parsed_coco_output):
        anns, imgs, cats = parsed_coco_output
        assert len(anns['image_id'].unique()) == len(imgs)

    def test_each_annotation_have_existing_category(self, parsed_coco_output):
        anns, imgs, cats = parsed_coco_output
        assert anns['category_id'].isin(cats['id']).all()

