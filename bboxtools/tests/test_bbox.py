from bboxtools.core.bbox import TLBR_BBox, TLWH_BBox, CWH_BBox

source_tlbr = TLBR_BBox("car", "test.jpg", 1, 3, 5, 1, 0.22, 1920, 1080)
source_tlwh = TLWH_BBox("car", "test.jpg", 1, 3, 4, 2, 0.22, 1920, 1080)
source_cwh = CWH_BBox("car", "test.jpg", 3, 2, 4, 2, 0.22, 1920, 1080)

def test_tlbr():
    source_tlbr = TLBR_BBox("car", "test.jpg", 1, 3, 5, 1, 0.22, 1920, 1080)
    source_tlwh = TLWH_BBox("car", "test.jpg", 1, 3, 4, 2, 0.22, 1920, 1080)
    source_cwh = CWH_BBox("car", "test.jpg", 3, 2, 4, 2, 0.22, 1920, 1080)

    assert source_tlbr == TLBR_BBox.from_TLWH(source_tlwh)
    assert source_tlbr == TLBR_BBox.from_CWH(source_cwh)

def test_tlwh():
    source_tlbr = TLBR_BBox("car", "test.jpg", 1, 3, 5, 1, 0.22, 1920, 1080)
    source_tlwh = TLWH_BBox("car", "test.jpg", 1, 3, 4, 2, 0.22, 1920, 1080)
    source_cwh = CWH_BBox("car", "test.jpg", 3, 2, 4, 2, 0.22, 1920, 1080)

    assert source_tlwh == TLWH_BBox.from_TLBR(source_tlbr)
    assert source_tlwh == TLWH_BBox.from_CWH(source_cwh)

def test_cwh():
    source_tlbr = TLBR_BBox("car", "test.jpg", 1, 3, 5, 1, 0.22, 1920, 1080)
    source_tlwh = TLWH_BBox("car", "test.jpg", 1, 3, 4, 2, 0.22, 1920, 1080)
    source_cwh = CWH_BBox("car", "test.jpg", 3, 2, 4, 2, 0.22, 1920, 1080)

    assert source_cwh == CWH_BBox.from_TLBR(source_tlbr)
    assert source_cwh == CWH_BBox.from_TLWH(source_tlwh)
