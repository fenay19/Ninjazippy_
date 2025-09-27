"""Core functionality for creating and extracting .7z archives using py7zr."""

import os
import logging
import py7zr

logger = logging.getLogger(__name__)


class NinjaZipError(Exception):
    """Custom exception for NinjaZipPy errors."""


def _ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)


def create_7z(archive_path: str, sources: list[str], compression_level: int = 5) -> None:
    """
    Create a .7z archive containing the given sources.
    """
    archive_path = os.path.abspath(archive_path)
    if not sources:
        raise NinjaZipError("No sources provided to archive")

    _ensure_parent_dir(archive_path)

    try:
        with py7zr.SevenZipFile(archive_path, mode="w") as archive:
            for s in sources:
                s_abs = os.path.abspath(s)
                if not os.path.exists(s_abs):
                    raise NinjaZipError(f"Source not found: {s}")
                arcname = os.path.basename(s_abs.rstrip(os.sep))
                if os.path.isdir(s_abs):
                    archive.writeall(s_abs, arcname=arcname)
                else:
                    archive.write(s_abs, arcname=arcname)
    except Exception as exc:
        logger.exception("Failed to create archive %s", archive_path)
        raise NinjaZipError(str(exc)) from exc


def extract_7z(archive_path: str, dest_dir: str = ".", overwrite: bool = True) -> None:
    """
    Extract a .7z archive to the given destination directory.
    """
    archive_path = os.path.abspath(archive_path)
    if not os.path.exists(archive_path):
        raise NinjaZipError(f"Archive not found: {archive_path}")

    dest = os.path.abspath(dest_dir)
    os.makedirs(dest, exist_ok=True)

    try:
        with py7zr.SevenZipFile(archive_path, mode="r") as archive:
            archive.extractall(path=dest)
    except Exception as exc:
        logger.exception("Failed to extract archive %s", archive_path)
        raise NinjaZipError(str(exc)) from exc
