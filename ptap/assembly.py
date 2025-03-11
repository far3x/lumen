from ptap.file_reader import read_file
from typing import List
import os

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
    return files_list

def add_intro(prompt: str, intro: str):
    prompt += intro + space

def add_structure(prompt: str, json_structure: str):
    prompt += json_structure + space

def add_files_content(prompt: str, files_root: dict):
    #file title then file content added in the prompt
    for file_name, file_path in files_root.keys():
        prompt += file_name + space #specify in the prompt the path and which file we're reading
        prompt += read_file(file_path) + space #specify in the prompt the content of that file