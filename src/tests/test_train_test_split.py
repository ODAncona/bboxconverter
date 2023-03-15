import pytest
import bboxconverter as bc
from pathlib import Path
import json
import pandas as pd
import shutil

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
    yield output_path, parser
    output_path.unlink()


@pytest.fixture
def train_test_split(export_csv_to_coco):
    original_path, parser = export_csv_to_coco
    parser.export(original_path, format="coco", split=True)
    file_name = original_path.name
    train_path = Path(original_path.parent / "train" / file_name)
    test_path = Path(original_path.parent / "test" / file_name)
    yield file_name, train_path, test_path, original_path, parser
    shutil.rmtree(train_path.parent)
    shutil.rmtree(test_path.parent)


class TestClass():
    def test_train_test_split_no_data_lost(self, train_test_split):
        file_name, train_path, test_path, original_path, parser = train_test_split
        train_annotation = train_path.parent / file_name
        test_annotation = test_path.parent / file_name
        parser_train = bc.read_coco(train_annotation)
        parser_test = bc.read_coco(test_annotation)
        assert len(parser.data) == len(parser_train.data) + len(parser_test.data)

    def test_train_test_split_no_annotations_lost(self, train_test_split):
        file_name, train_path, test_path, original_path, parser = train_test_split
        train_annotation = train_path.parent / file_name
        test_annotation = test_path.parent / file_name
        parser_train = bc.read_coco(train_annotation)
        parser_test = bc.read_coco(test_annotation)
        cnt = parser.data['file_path'].value_counts()
        cnt_train = parser_train.data['file_path'].value_counts()
        cnt_test = parser_test.data['file_path'].value_counts()
        assert (pd.concat([cnt_train, cnt_test], axis=0) == cnt).all()

