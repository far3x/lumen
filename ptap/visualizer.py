import os
from typing import List
import json


def get_project_structure(root_path: str, skipped_folders: List):
    root_path_name = "".join(root_path.split("/")[-1]) + "/"
    structure = {root_path_name: {}}

    for root, directories, files in os.walk(root_path, topdown = True):
        if any(root.endswith(folder) for folder in skipped_folders):
            directories[:] = []
            structure[root_path_name]["".join(root.split("\\")[-1]) + "/"] = {}
            continue

        base = structure[root_path_name]
        level = len(root.split("\\")) - len(root_path.split("\\"))
        
        for x in range(level, 0, -1):
            folder_subname = root.split("\\")[-x]
            if x == 1:
                base[f"{folder_subname}/"] = {}
                if files:
                    for file in files:
                        base["".join({folder_subname}) + "/"][file] = {}
            else:
                base = base[folder_subname + "/"]

    return structure

path = "output.json"
with open(path, "w") as file:
    json.dump(get_project_structure(root_path = "C:/Users/far30/Downloads/GENERATION MEMOIRE TECHNIQUE API", skipped_folders = [".git", "__pycache__"]),
              file,
              indent = 4
              )


"""

WHAT WE WANT: (in a structured json first, then formatted correctly and visually appealing for AI)

main_directory/
 ├── dir0/
 |    └── special_file.txt
 ├── dir1/
 |    ├── file2.txt
 |    └── file1.txt
 ├── dir2/
 |    ├── subdir2/
 |    └── subdir1/
 |         ├── file_in_subdir1.txt
 |         └── subsubdir1/
 |              └── deep_file.txt
 ├── empty_dir/
 └── root_file.txt

"""