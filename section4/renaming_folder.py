from pathlib import Path
import shutil as sh

common_path = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
src_folder = common_path / "final_folder"
dest_folder = common_path / "renamed_folder"

if src_folder.exists():
    sh.move(src=src_folder, dst=dest_folder)

# what if we want to copy and renaming at the same time ?

common_path_file = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
src_file = common_path_file / "bad_jokes.csv"
dest_file = common_path_file / "renamed_folder" / "sad_jokes.csv"

if src_file.exists():
    sh.move(src=src_file, dst=dest_file)
