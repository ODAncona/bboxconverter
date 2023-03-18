import pytest
import bboxconverter as bc
from pathlib import Path
from os import unlink
import pandas as pd

@pytest.fixture
def read_pascal_voc():
    input_path = Path("src/tests/test_data/pascal_voc/")
    parser = bc.read_pascal_voc(input_path)
    return parser

@pytest.fixture
def read_csv():
    input_path = Path("src/tests/test_data/cat_dog.csv")
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
    parser.to_csv("src/tests/test_data/cat_dog_tlbr.csv", type="tlbr")
    parser2 = bc.read_csv("src/tests/test_data/cat_dog_tlbr.csv")
    yield parser2
    unlink("src/tests/test_data/cat_dog_tlbr.csv")

class TestClass():
    def test_all_columns_should_be_present(self, read_pascal_voc):
        parsed_columns = set(read_pascal_voc.data.columns)
        official_col = set(['file_path', 'class_name', 'x_min', 'y_min', 'x_max', 'y_max', 'image_width', 'image_height'])
        assert official_col.issubset(parsed_columns)

    def test_all_images_should_be_parsed(self, read_pascal_voc):
        annotation_path = Path("src/tests/test_data/pascal_voc/Annotations")
        xml_files = [x for x in annotation_path.iterdir() if x.suffix == ".xml"]
        assert len(read_pascal_voc.data['file_path'].unique()) == len(xml_files)

    def test_dataset_should_be_the_same_as_csv(self, read_pascal_voc, read_csv):
        data_pascal_voc = read_pascal_voc.data.sort_index()
        data_csv_tlbr = read_csv.data.sort_index()
        parsed_bbox = data_pascal_voc[['x_min', 'y_min', 'x_max', 'y_max']].describe()
        csv_bbox = data_csv_tlbr[['x_min', 'y_min', 'x_max', 'y_max']].describe()
        std_comp = abs(parsed_bbox.loc['std'] / csv_bbox.loc['std'])
        
        assert sum(std_comp) > 3.96 and sum(std_comp) < 4.04
    

 
    
    