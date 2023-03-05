# Bounding Box Reference

To easily convert a bounding box to different format, a bounding box should have the following attributes:

- `class_name`
- `file_path`
- `x_min`
- `y_min`
- `x_max`
- `y_max`
- `x_center`
- `y_center`
- `width`
- `height`
- `confidence`
- `image_height`
- `image_width`
- `image_channels`

**Mandatory**

- class_name
- file_path

**Format Specific**

| TLBR                                                              |                                   CWH                                    | TLWH                                                               |
| ----------------------------------------------------------------- | :----------------------------------------------------------------------: | ------------------------------------------------------------------ |
| <ul><li>x_min</li><li>y_min</li><li>x_max</li><li>y_max</li></ul> | <ul><li>x_center</li><li>y_center</li><li>width</li><li>height</li></ul> | <ul><li>x_min</li><li>y_min</li><li>width</li><li>height</li></ul> |

**Metadata**

- confidence
- image_height
- image_width
- image_channel

```mermaid
---
title: Bounding Box Generic Class
---
classDiagram
    class BBox {
    BBox : class_name
    BBox : file_path
    BBox : x_min
    BBox : y_min
    BBox : x_max
    BBox : y_max
    BBox : x_center
    BBox : y_center
    BBox : width
    BBox : height
    BBox : confidence
    BBox : image_height
    BBox : image_width
    BBox : image_channel
    BBox: __str__()
    BBox: __eq__()
    }
    class TLWH_BBox{
    TLWH_BBox : x_min
    TLWH_BBox : y_min
    TLWH_BBox : width
    TLWH_BBox : height
    TLWH_BBox : from_TLBR()
    TLWH_BBox : from_CWH()
    }
    class TLBR_BBox{
    TLBR_BBox : x_min
    TLBR_BBox : y_min
    TLBR_BBox : x_max
    TLBR_BBox : y_max
    TLBR_BBox : from_TLWH()
    TLBR_BBox : from_CWH()
    }
    class CWH_BBox{
    CWH_BBox : x_center
    CWH_BBox : y_center
    CWH_BBox : width
    CWH_BBox : height
    CWH_BBox : from_TLWH()
    CWH_BBox : from_TLBR()
    }
```
