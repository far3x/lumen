import os
from typing import List

def get_project_structure(root_path: str, skipped_folders: List):
    root_path_name = "".join(root_path.split(os.sep)[-1]) + "/"
    structure = {root_path_name: {}}

    for root, directories, files in os.walk(root_path, topdown = True):
        if any(root.endswith(folder) for folder in skipped_folders):
            directories[:] = []
            structure[root_path_name]["".join(root.split(os.sep)[-1]) + "/"] = {} #.join used bcs cant use f string inside dict reading
            continue

        base = structure[root_path_name]
        level = len(root.split(os.sep)) - len(root_path.split(os.sep)) #start at 1 and ends at biggest level

        if level == 0:
            if files:
                for file in files:
                    base[file] = {}
        else:
            for x in range(level, 0, -1):
                folder_subname = root.split(os.sep)[-x]
                if x == 1:
                    base[f"{folder_subname}/"] = {}
                    if files:
                        for file in files:
                            base[f"{folder_subname}/"][file] = {}
                            
                else:
                    base = base[folder_subname + "/"]

    return structure