from importlib.metadata import version, PackageNotFoundError
from . import device
from . import dtype
from . import data

try:
    __version__ = version("nanoml")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "device",
    "dtype",
    "data",
]
