"""

Attributes
----------
FORMAT : list
    List of supported formats. Can be one of the following: 'voc', 'coco', 'yolo', 'jsonlines'

TYPES : list
    List of supported bounding box types. Can be one of the following: 'tlbr', 'tlwh', 'cwh'
"""
from pandas.core.frame import DataFrame
from sklearn.model_selection import GroupShuffleSplit, GroupKFold
from bboxconverter.core.bbox import BBox, TLBR_BBox, TLWH_BBox, CWH_BBox
from bboxconverter.io.writer_coco import to_coco
from bboxconverter.io.writer_yolo import to_yolo
from bboxconverter.io.writer_pascal_voc import to_pascal_voc
from pathlib import Path
from shutil import copy

FORMAT = ["voc", "coco", "yolo", "jsonlines"]
TYPES = ["tlbr", "tlwh", "cwh"]


class BboxParser:
    """
    The BboxParser class is used to ingest bounding boxes from various format into a pandas dataframe and output them in various formats.
    """

    data: DataFrame = None
    bbox_type: str = None

    def __init__(self, data: DataFrame, bbox_type) -> None:
        """
        Initialize BboxParser object

        Parameters
        ----------
        data : DataFrame
            Dataframe containing generic bounding boxes. Could contains some of the following columns:
                -'class_name'
                -'file_path'
                -'x_min'
                -'y_min'
                -'x_max'
                -'y_max'
                -'x_center'
                -'y_center'
                -'width'
                -'height'
                -'confidence'
                -'image_height'
                -'image_width'
                -'image_channels'

        bbox_type : str
            Type of bounding box. Can be one of the following: 'tlbr', 'tlwh', 'cwh'
        """
        self.data = data
        self.bbox_type = bbox_type

    def create_bbox(self, bbox_type: str, **kwargs) -> BBox:
        """
        Create bounding box object from a dictionary of parameters

        Parameters
        ----------
        bbox_type : str
            Type of bounding box. Can be one of the following: 'tlbr', 'tlwh', 'cwh'
        **kwargs : dict
            Dictionary of parameters for bounding box
        """
        if bbox_type == "tlbr":
            return TLBR_BBox(**kwargs)
        if bbox_type == "tlwh":
            return TLWH_BBox(**kwargs)
        if bbox_type == "cwh":
            return CWH_BBox(**kwargs)
        return None

    def create_data_splits(
        self,
        ds_path,
        train_size=0.8,
        val_size=0.1,
        test_size=0.1,
        save_func=to_coco,
    ) -> None:
        if train_size + val_size + test_size != 1:
            raise ValueError("train_size + val_size + test_size must equal 1.0")

        ds_path = Path(ds_path)

        # Group split
        splitter1 = GroupShuffleSplit(
            train_size=train_size + val_size,
            test_size=test_size,
            n_splits=1,
            random_state=7,
        )
        split = splitter1.split(self.data, groups=self.data["file_path"])
        temp_inds, test_inds = next(split)
        temp = self.data.iloc[temp_inds]
        test = self.data.iloc[test_inds]

        # Split temp into train and val
        splitter2 = GroupShuffleSplit(
            train_size=train_size / (train_size + val_size),
            test_size=val_size / (train_size + val_size),
            n_splits=1,
            random_state=7,
        )
        split = splitter2.split(temp, groups=temp["file_path"])
        train_inds, val_inds = next(split)
        train = temp.iloc[train_inds]
        val = temp.iloc[val_inds]

        # Management
        splits = dict(
            train=dict(ds=train, path=ds_path / "train", output_name="train.json"),
            val=dict(ds=val, path=ds_path / "val", output_name="val.json"),
            test=dict(ds=test, path=ds_path / "test", output_name="test.json"),
        )

        for split in splits.values():
            # Create directories
            split_path = split["path"]
            img_folder = split_path / "images"
            split_path.mkdir(parents=True, exist_ok=True)
            img_folder.mkdir(parents=True, exist_ok=True)

            # Copy images
            for img in split["ds"]["file_path"].unique():
                copy(ds_path / img, img_folder / Path(img).name)

            # Save annotations
            save_func(split["ds"], str(split["path"] / split["output_name"]))

    def create_kfold_splits(
        self,
        ds_path,
        kfold,
        train_size=0.8,
        test_size=0.2,
        save_func=to_coco,
    ) -> None:
        """
        Create kfold splits of the dataset and save them in the specified format

        Parameters
        ----------
        ds_path : str | Path
            Path to dataset
        kfold : int
            Number of folds
        train_size : float
            Size of the train split
        test_size : float
            Size of the test split
        save_func : function
            Function to convert bbox
        """
        ds_path = Path(ds_path)

        group_kfold = GroupKFold(n_splits=kfold)

        for i, (train_index, test_index) in enumerate(
            group_kfold.split(self.data, groups=self.data["file_path"]), start=1
        ):
            print(f"Creating fold {i} of {kfold}")
            # Create directories
            split_path = ds_path / f"fold_{i}"
            split_path.mkdir(parents=True, exist_ok=True)

            # Create train and test splits
            train = self.data.iloc[train_index]
            test = self.data.iloc[test_index]

            # Management
            splits = dict(
                train=dict(ds=train, path=split_path / "train", output_name="train.json"),
                test=dict(ds=test, path=split_path / "test", output_name="test.json"),
            )

            for split in splits.values():
                # Create directories
                split_path = split["path"]
                split_path.mkdir(parents=True, exist_ok=True)

                # Save annotations
                save_func(split["ds"], str(split["path"] / split["output_name"]))

    def export(
        self,
        output_path: "str | Path",
        format: str,
        split=False,
        train_size=0.8,
        test_size=0.1,
        val_size=0.1,
        kfold=None,
    ) -> None:
        """
        Export bounding boxes to a popular file format:

        - "voc" => Pascal VOC
        - "coco" => COCO
        - "yolo" => YOLO
        - "jsonlines" => Sagemaker

        If split is False, the output file will contain all bounding boxes. If split is True, the output file will contain the train and test split of the dataset.

        If kfold is not None, the output folder will contain the kfold split of the dataset.

        Parameters
        ----------
        output_path : str | Path
            Path to output folder. It will add the file name and extension automatically.
        format : str
            Format of output file. Can be one of the following: 'voc', 'coco', 'yolo', 'sagemaker'
        type : str
            Type of bounding box. Can be one of the following: 'tlbr', 'tlwh', 'cwh'
        split : bool
            Split the dataset into train and test using scikit-learn train_test_split function.
        train_size : float
            If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size.
        test_size : float
            If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.
        kfold : int
            Number of folds to split the dataset into. If None, the dataset will not be split into folds.

        """
        df_bbox = self.data.copy()

        # Check if bounding box type is set
        type = self.bbox_type
        assert type is not None
        if type not in TYPES:
            raise ValueError(f"Invalid bbox type: {type}")

        # Set export to file function
        save_func = {"coco": to_coco, "voc": to_pascal_voc, "yolo": to_yolo}.get(
            format, None
        )
        if save_func is None:
            raise ValueError(f"Invalid save function: {format}")

        format_type = {"coco": "tlwh", "voc": "tlbr", "yolo": "cwh"}

        # Check if we need to convert bounding boxes
        if type != format_type[format]:
            # Set conversion function
            format_map = {
                ("voc", "tlwh"): TLBR_BBox.from_TLWH,
                ("voc", "cwh"): TLBR_BBox.from_CWH,
                ("coco", "tlbr"): TLWH_BBox.from_TLBR,
                ("coco", "cwh"): TLWH_BBox.from_CWH,
                ("yolo", "tlbr"): CWH_BBox.from_TLBR,
                ("yolo", "tlwh"): CWH_BBox.from_TLWH,
            }

            # Get conversion function
            convert_func = format_map.get((format.lower(), type))
            if convert_func is None:
                raise ValueError(f"Invalid export format: {format}")

            # Transform data to bounding boxes
            bboxes = df_bbox.drop(columns=["image_channel"], errors="ignore").apply(
                lambda x: self.create_bbox(self.bbox_type, **x.to_dict()), axis=1
            )

            # Serialize bounding boxes
            bboxes = bboxes.apply(lambda x: convert_func(x).to_dict())
            df_bbox = DataFrame.from_records(bboxes)

        # Save to file
        if split:
            self.create_data_splits(
                output_path, train_size, test_size, val_size, save_func
            )
        if kfold:
            self.create_kfold_splits(
                output_path, kfold, train_size, test_size, save_func
            )
        else:
            save_func(df_bbox, Path(output_path) / "annotations.json")

    def to_csv(self, output_path: "str | Path", type) -> None:
        """
        Export bounding boxes to a csv file.

        Parameters
        ----------
        output_path : str | Path
            Path to output file
        type : str
            Type of bounding box. Can be one of the following: 'tlbr', 'tlwh', 'cwh'
        """
        assert self.bbox_type is not None
        if type not in TYPES:
            raise ValueError(f"Invalid bbox type: {type}")

        # Conversion function map (output_type, input_bbox_type)
        # Each type should have two functions to convert from TLBR, TLWH, CWH
        type_map = {
            ("tlbr", "tlwh"): TLBR_BBox.from_TLWH,
            ("tlbr", "cwh"): TLBR_BBox.from_CWH,
            ("tlwh", "tlbr"): TLWH_BBox.from_TLBR,
            ("tlwh", "cwh"): TLWH_BBox.from_CWH,
            ("cwh", "tlbr"): CWH_BBox.from_TLBR,
            ("cwh", "tlwh"): CWH_BBox.from_TLWH,
        }

        if type == self.bbox_type:
            # No conversion needed
            self.data.to_csv(output_path, index=False)
            return

        # Get conversion function
        convert_func = type_map.get((type, self.bbox_type))

        if convert_func is None:
            raise ValueError(f"Invalid bbox type: {type}")

        # Transform data to bounding boxes
        bboxes = self.data.drop(columns=["image_channel"], errors="ignore").apply(
            lambda x: self.create_bbox(self.bbox_type, **x.to_dict()), axis=1
        )

        # Serialize bounding boxes
        bboxes = bboxes.apply(lambda x: convert_func(x).to_dict())

        # Save to file
        DataFrame.from_records(bboxes).to_csv(output_path, index=False)

    def __str__(self) -> str:
        return self.data.to_string()
