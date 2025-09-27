import os
from lum.gitignore import *
from typing import List

def get_project_structure(root_path: str, skipped_folders: List):
    #this function looks abit hard, basically will take the root path, format it correctly
    #to show it in the prompt (with a /... etc), will check first folders, level by level
    #then files, when adding folders, little format change -> "/" added
    root_path_name = "".join(root_path.split(os.sep)[-1]) + "/"
    structure = {root_path_name: {}}

    if gitignore_exists(""):
        _, skipped_folders = gitignore_skipping()
    
    for root, _, files in os.walk(root_path, topdown = True):
        #skipping folders starting with "."
        relative_dir = os.path.relpath(root, root_path)
        if any(part.startswith('.') for part in relative_dir.split(os.sep) if part != '.'):
            _[:] = []
            continue

        should_skip = False
        for folder_name in skipped_folders:
            #in skipped_folders, if starts wiht "*" -> will skip anything that ENDS with the skipped folder name, otherwise will take the folder name directly, and ONLY this
            if folder_name.startswith("*"):
                if root.endswith(folder_name[1::]): #remove the * and set condition
                    _[:] = []
                    structure[root_path_name][f"{''.join(root.split(os.sep)[-1])}/"] = {}
                    should_skip = True
                    break

            else:
                element = root.split(os.sep)[-1]
                if element == folder_name:
                    _[:] = []
                    structure[root_path_name][f"{''.join(root.split(os.sep)[-1])}/"] = {}
                    should_skip = True
                    break

        if should_skip:
            continue


        base = structure[root_path_name]
        level = len(root.split(os.sep)) - len(root_path.split(os.sep)) #starts at 1, ends at highest level

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