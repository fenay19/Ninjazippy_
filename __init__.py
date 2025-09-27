"""NinjaZipPy package — simple Python 7z archiver."""

from .core import create_7z, extract_7z, NinjaZipError

__all__ = ["create_7z", "extract_7z", "NinjaZipError"]
