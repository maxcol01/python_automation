from pathlib import Path
import shutil as sh

src = Path.home() / "Desktop" / "dad_jokes.csv"

folder_path = Path(".") / "python_automation" / "copying_stuff"
folder_path.mkdir(exist_ok=True)
dest_path = folder_path / "dad_jokes.csv"

#  to copy we need to specify a source path and a destination path !
if not src.exists():
    print("the source file does not exist")
elif dest_path.exists():
    print("the file already exists")
else:
    sh.copy(src, folder_path)

#  Now when copying we need to kepp in mind:
#  - is the file exist ?
#  - is there already a file in the destination ?

# copying folder is the same as for files (we simply need to reference folder paths)
#  as well as using the copytree() method from shutil. this is specificaly designed for
#  folder copying !

folder_src = Path(".") / "python_automation" / "fun_w_folder"
folder_dest = Path(".") / "python_automation" / "copying_stuff" / "fun_w_folder"

if not folder_dest.exists():
    sh.copytree(src=folder_src, dst=folder_dest, dirs_exist_ok=True)
else:
    print("the folder already exits")
    #  or using dir_exists_ok = True