from pathlib import Path

#  to create a new folder we need to specify the path and a name in our Path object !

new_folder = Path(".") / "python_automation"
if not new_folder.exists():
    new_folder.mkdir()
#     another way would be to add a parameter in the mkdir() method
#     new_folder.mkdir(exist_ok=True)

# Note that we cannot create a folder within a folder that does not exist ! At least not like that
#  we need to add another argument to the mkdir method. Setting parents=True indicates to create any
#  parent folder if they do not exist

another_folder = new_folder / "fun_w_folder" / "final_folder"
another_folder.mkdir(exist_ok=True, parents=True)
