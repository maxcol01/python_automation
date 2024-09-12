from pathlib import Path
import shutil as sh

# Note: when renaming a file, it is essentially the same as moving it since the
# name of a file/folder is linked to its location, aka its path !
# so by moving it to the same location BUT changing its name (in its path)
# essentially changes its name !

common_path = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
src_file = common_path / "dad_jokes.csv"
dest_file = common_path / "bad_jokes.csv"

if src_file.exists():
    sh.move(src=src_file, dst=dest_file)