import pytest
import bboxconverter as bc
from pathlib import Path
import json
import pandas as pd
import shutil

@pytest.fixture
def export_csv_to_coco():
    input_path = Path("src/tests/test_data/cat_dog.csv")
    output_path = Path("src/tests/test_data/")
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
    #output_path = output_path / "annotations.json"
    yield output_path, parser
    (output_path / "annotations.json").unlink()


@pytest.fixture
def train_test_split(export_csv_to_coco):
    original_path, parser = export_csv_to_coco
    parser.export(original_path, format="coco", split=True)
    train_path = Path(original_path / "train" / "train.json")
    test_path = Path(original_path / "test" / "test.json")
    val_path = Path(original_path / "val" / "val.json")
    yield original_path, parser
    shutil.rmtree(train_path.parent)
    shutil.rmtree(test_path.parent)
    shutil.rmtree(val_path.parent)


class TestClass():
    def test_train_test_split_no_data_lost(self, train_test_split):
        original_path, parser = train_test_split
        train_path = original_path / "train" / "train.json"
        test_path = original_path / "test" / "test.json"
        val_path = original_path / "val" / "val.json"
        parser_train = bc.read_coco(train_path)
        parser_test = bc.read_coco(test_path)
        parser_val = bc.read_coco(val_path)
        assert len(parser.data) == len(parser_train.data) + len(parser_test.data) + len(parser_val.data)

    def test_train_test_split_no_annotations_lost(self, train_test_split):
        original_path, parser = train_test_split
        train_path = original_path / "train" / "train.json"
        test_path = original_path / "test" / "test.json"
        val_path = original_path / "val" / "val.json"
        parser_train = bc.read_coco(train_path)
        parser_test = bc.read_coco(test_path)
        parser_val = bc.read_coco(val_path)
        cnt = parser.data['file_path'].value_counts().sort_index()
        cnt_train = parser_train.data['file_path'].value_counts()
        cnt_test = parser_test.data['file_path'].value_counts()
        cnt_val = parser_val.data['file_path'].value_counts()
        reconstruction = pd.concat([cnt_train, cnt_test, cnt_val], axis=0).sort_index()
        assert (reconstruction.index == cnt.index).all()

