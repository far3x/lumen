import os
from typing import List
import json

def get_project_structure(root_path: str, skipped_folders: List):
    root_path_name = "".join(root_path.split("/")[-1]) + "/"
    structure = {root_path_name: {}}

    for root, directories, files in os.walk(root_path, topdown = True):
        if any(root.endswith(folder) for folder in skipped_folders):
            directories[:] = []
            structure[root_path_name]["".join(root.split("\\")[-1]) + "/"] = {} #.join used bcs cant use f string when reading a list !
            continue

        base = structure[root_path_name]
        level = len(root.split("\\")) - len(root_path.split("\\")) #start at 1 ends at max

        if level == 0:
            if files:
                for file in files:
                    base[file] = {}
        else:
            for x in range(level, 0, -1):
                folder_subname = root.split("\\")[-x]
                if x == 1:
                    base[f"{folder_subname}/"] = {}
                    if files:
                        for file in files:
                            base[f"{folder_subname}/"][file] = {}
                            
                else:
                    base = base[folder_subname + "/"]

    return structure

json_file = "temp_structure.json"
with open(json_file, "w") as file:
    json.dump(get_project_structure(root_path = "C:/Users/far30/Downloads/GENERATION MEMOIRE TECHNIQUE API", 
                                    skipped_folders = [".git", "__pycache__"]),
              file,
              indent = 4 #number of spaces for the indentation in the json file, didn't know !!
    )
