from importlib.metadata import version, PackageNotFoundError
from . import device
from . import dtype

try:
    __version__ = version("nanoml")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "device",
    "dtype",
]
