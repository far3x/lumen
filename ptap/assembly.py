from ptap.file_reader import *
from typing import List
import os


PROMPT_SEPERATOR = "\n\n\n"

def get_files_root(main_root: str, skipped_folders: List, allowed: List = allowed_files):
    files_list = {}
    min_level = 0
    for root, _, files in os.walk(main_root):
        if any(root.endswith(folder) for folder in skipped_folders):
            _[:] = []
            continue
        if min_level == 0:
            min_level = len(main_root.split(os.sep))
        if files:
            for file in files:
                if any(file.endswith(allowed_file) for allowed_file in allowed):
                    file_root = f"{root}{os.sep}{file}"
                    file_list_index = "/".join(file_root.split(os.sep)[min_level::])
                    files_list[file_list_index] = file_root
    return files_list

def add_intro(prompt: str, intro: str):
    prompt += intro + PROMPT_SEPERATOR
    return prompt

def add_structure(prompt: str, json_structure: str):
    prompt += json_structure + PROMPT_SEPERATOR
    return prompt

def add_files_content(prompt: str, files_root: dict, show_title: bool = True, title_text: str = None):
    #file title then file content added in the prompt
    for file_name, file_path in files_root.items():
        if show_title: 
            prompt += title_text.format(file = file_name) + PROMPT_SEPERATOR #specify in the prompt the path and which file we're reading
        prompt += read_file(file_path) + PROMPT_SEPERATOR #specify in the prompt the content of that file
    return prompt