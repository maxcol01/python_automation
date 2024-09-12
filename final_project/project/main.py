from pathlib import Path
from zipfile import ZipFile


def unzip_file(path: Path) -> None:
    """
    function to unzip my file and delete the .zip file
    :return: None
    """
    with ZipFile(path, mode="r") as zip_file:
        zip_file.extractall(path=Path(".") / "data")

    # deleting file
    path.unlink()


path_zip = Path(".") / "clean_sweep_example_folder.zip"
is_zipped = False

if is_zipped:
    unzip_file(path=path_zip)
