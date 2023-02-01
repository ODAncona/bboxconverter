from bbox import BBox, TLBR_BBox, TLWH_BBox, CWH_BBox

source_tlbr = TLBR_BBox("car", "test.jpg", 1, 3, 5, 1, 0.22, 1920, 1080)
source_tlwh = TLWH_BBox("car", "test.jpg", 1, 3, 4, 2, 0.22, 1920, 1080)
source_cwh = CWH_BBox("car", "test.jpg", 3, 2, 4, 2, 0.22, 1920, 1080)

print(source_tlbr)
print(source_tlwh)
print(source_cwh)

print("_____________________TLBR_______________________")

# TLBR
print(TLBR_BBox.from_TLWH(source_tlwh))
print(TLBR_BBox.from_CWH(source_cwh))

print("_____________________TLWH___________________________")

# TLWH
print(TLWH_BBox.from_TLBR(source_tlbr))
print(TLWH_BBox.from_CWH(source_cwh))

print("______________________CWH____________________________")

# CWH
print(CWH_BBox.from_TLBR(source_tlbr))
print(CWH_BBox.from_TLWH(source_tlwh))
