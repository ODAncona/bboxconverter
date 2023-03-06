from bboxconverter.core.bbox import TLBR_BBox, TLWH_BBox, CWH_BBox

source_tlbr = TLBR_BBox("car", "test.jpg", 98, 345, 420, 462, 0.82, 640, 480)
source_tlwh = TLWH_BBox("car", "test.jpg", 98, 345, 322, 117, 0.82, 640, 480)
source_cwh = CWH_BBox("car", "test.jpg", 0.4046875,
                      0.840625, 0.503125, 0.24375, 0.82, 640, 480)

'''
https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/
As an example, we will use an image from the dataset named Common Objects in Context. 
It contains one bounding box that marks a cat. The image width is 640 pixels, and its height is 480 pixels. 
The width of the bounding box is 322 pixels, and its height is 117 pixels.

The bounding box has the following (x, y) coordinates of its corners: 
- top-left is (x_min, y_min) or (98px, 345px), 
- top-right is (x_max, y_min) or (420px, 345px), 
- bottom-left is (x_min, y_max) or (98px, 462px), 
- bottom-right is (x_max, y_max) or (420px, 462px). 
As you see, coordinates of the bounding box's corners are calculated with respect to the top-left corner of the image which has (x, y) coordinates (0, 0).
'''


class TestBBox:

    def test_to_tlbr_conversion(self):
        assert source_tlbr == TLBR_BBox.from_TLWH(source_tlwh)
        assert source_tlbr == TLBR_BBox.from_CWH(source_cwh)

    def test_to_tlwh_conversion(self):
        assert source_tlwh == TLWH_BBox.from_TLBR(source_tlbr)
        assert source_tlwh == TLWH_BBox.from_CWH(source_cwh)

    def test_to_cwh_conversion(self):
        assert source_cwh == CWH_BBox.from_TLBR(source_tlbr)
        assert source_cwh == CWH_BBox.from_TLWH(source_tlwh)
