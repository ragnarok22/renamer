import logging
import re
import sys
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def renamer(file_path: Path, new_name: str) -> bool:
    """
    Renames a file
    """
    try:
        file_path.rename(file_path.parent / new_name)
        return True
    except Exception as e:
        logger.error(e)
        return False


def rename_download_files_from_youtube(dir_path: str) -> None:
    """
    Renames all files in a directory to their corresponding video title
    """
    try:
        dir_path = Path(dir_path)
        for file in dir_path.iterdir():
            if file.suffix == ".part":
                continue
            new_name = file.stem.replace("_", " ").replace(" - 10Convert.com.mp4", "").strip()
            new_name = re.sub(r"\s+", " ", new_name) + file.suffix
            logger.info(f"Renaming {file.name} to {new_name}")
            renamer(file, new_name)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    dir_path_to_rename = sys.argv[1] if len(sys.argv) > 1 else "/home/ragnarok/Downloads"
    rename_download_files_from_youtube(dir_path_to_rename)
