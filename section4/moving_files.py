from pathlib import Path
import shutil as sh

# Create a folder
new_folder = Path(".") / "python_automation" / "copying_stuff" / "moving_folder"
# Check its existence and make sure the entire folder is copied !
new_folder.mkdir(exist_ok=True, parents=True)

src_folder = Path(".") / "python_automation" / "copying_stuff" / "dad_jokes.csv"
dest_folder = new_folder / "dad_jokes.csv"

if src_folder.exists():
    sh.move(src=src_folder, dst=dest_folder)
