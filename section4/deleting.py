import pathlib as pt
import shutil as sh

# Create a folder to store our toy files

folder_path = pt.Path(".") / "toy_folder"
new_folder_path = folder_path / "deleted_folder"
folder_path.mkdir(exist_ok=True, parents=True)
new_folder_path.mkdir(exist_ok=True, parents=True)

# Moving our toy files to the toy_folder:
dest_file = folder_path
for i in range(1, 4):
    src_file = pt.Path(".") / f"test{i}.txt"
    if src_file.exists():
        sh.move(src=src_file, dst=dest_file)

# delete file: use .unlink() method
src_file_delete = folder_path / "test1.txt"
src_file_delete.unlink(missing_ok=True)

# delete folder: use .rmdir() (directory empty)
src_folder_delete = new_folder_path
if src_folder_delete.exists():
    src_folder_delete.rmdir()

# What if the folder is not empty ? .rmtree() -> shutil module.
src_folder_delete_new = folder_path
if src_folder_delete_new.exists():
    sh.rmtree(src_folder_delete_new)

