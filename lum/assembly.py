from lum.smart_read import read_file
from lum.gitignore import *
from typing import List
import os


PROMPT_SEPERATOR = "\n\n\n"

def get_files_root(main_root: str, skipped_folders: List, allowed: List = None):
    if allowed is None:
        from lum.smart_read import get_files_parameters
        allowed = get_files_parameters()["allowed_files"]
    
    #if gitignore, add skipped folders to existing skipped folder file
    #print("3 - ", gitignore_exists("")) #debug
    if gitignore_exists(""):
        _, skipped_folders = gitignore_skipping() #skipped_files not used here then, so maybe optimization incoming !
    #print("4 - ", skipped_folders) #debug

    files_list = {}
    min_level = 0
    for root, _, files in os.walk(main_root):
        #print("5 - ", root) #debug
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
    prompt += "--- PROJECT STRUCTURE ---" + PROMPT_SEPERATOR
    prompt += json_structure + PROMPT_SEPERATOR
    return prompt


def add_files_content(prompt: str, files_root: dict, title_text: str = None):
    #file title then file content added in the prompt
    for file_name, file_path in files_root.items():
        prompt += title_text.format(file = file_name) + PROMPT_SEPERATOR #specify in the prompt the path and which file we're reading
        prompt += read_file(file_path) + PROMPT_SEPERATOR #specify in the prompt the content of that file
    return prompt