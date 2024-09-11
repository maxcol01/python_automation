from pathlib import Path
import shutil as sh

src = Path.home() / "Desktop" / "dad_jokes.csv"

folder_path = Path(".") / "python_automation" / "copying_stuff"
folder_path.mkdir(exist_ok=True)

#  to copy we need to specify a source path and a destination path !
sh.copy(src, folder_path)

