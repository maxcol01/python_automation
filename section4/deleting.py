import pathlib as pt
import shutil as sh

# Create a folder to store our toy files

folder_path = pt.Path(".") / "toy_folder"
folder_path.mkdir(exist_ok=True, parents=True)

# Moving our toy files to the toy_folder:
dest_file = folder_path
for i in range(1, 4):
    src_file = pt.Path(".") / f"test{i}.txt"
    if src_file.exists():
        sh.move(src=src_file, dst=dest_file)
