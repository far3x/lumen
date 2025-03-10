from file_reader import *
import os
from visualizer import *

space = "\n\n\n"

def get_files_root(main_root: str, skipped_folders: List):
    files_list = {}
    min_level = 0
    for root, _, files in os.walk(main_root):
        if any(root.endswith(folder) for folder in skipped_folders):
            _[:] = []
            continue
        if min_level == 0:
            min_level = len(main_root.split("\\"))
        if files:
            for file in files:
                file_root = f"{root}\\{file}"
                file_list_index = "/".join(file_root.split("\\")[min_level::])
                files_list[file_list_index] = file_root
    print(files_list)            
    return files_list
    

print(os.getcwd())
get_files_root(os.getcwd(), [".git", "__pycache__"])