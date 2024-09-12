from pathlib import Path
import shutil as sh

# Create a folder
new_folder = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
# Check its existence and make sure the entire folder is copied !
new_folder.mkdir(exist_ok=True, parents=True)

# Specify the src and dest folder
# Important note: always specify THE ENTIRE path of what we move !
src_folder = Path(".") / "python_automation" / "copying_stuff" / "dad_jokes.csv"
dest_folder = new_folder / "dad_jokes.csv"

if src_folder.exists():
    sh.move(src=src_folder, dst=dest_folder)

# Let's move the final_folder to fun_w_folder

src_folder2 = Path(".") / "python_automation" / "fun_w_folder" / "final_folder"
dest_folder2 = new_folder / "final_folder"
if src_folder2.exists():
    sh.move(src=src_folder2, dst=dest_folder2)
