try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._generic_qslider import QDoubleSlider
from ._labeled import (
    QLabeledDoubleRangeSlider,
    QLabeledDoubleSlider,
    QLabeledRangeSlider,
    QLabeledSlider,
)
from ._qrangeslider import QDoubleRangeSlider, QRangeSlider

__all__ = [
    "QDoubleRangeSlider",
    "QDoubleSlider",
    "QLabeledDoubleRangeSlider",
    "QLabeledDoubleSlider",
    "QLabeledRangeSlider",
    "QLabeledSlider",
    "QRangeSlider",
]
