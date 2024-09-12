from pathlib import  Path
import shutil as sh

common_path = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
src_folder = common_path / "final_folder"
dest_folder = common_path / "renamed_folder"

if src_folder.exists():
    sh.move(src=src_folder, dst=dest_folder)