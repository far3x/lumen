from lum.smart_read import read_file
from lum.gitignore import *
from lum.data import sanitize_code
from typing import List
import os


PROMPT_SEPERATOR = "\n\n\n"

def get_files_root(main_root: str, skipped_folders: List, allowed: List = None):
    if allowed is None:
        from lum.smart_read import get_files_parameters
        allowed = get_files_parameters()["allowed_files"]
    
    if gitignore_exists(""):
        _, skipped_folders = gitignore_skipping()

    files_list = {}
    min_level = 0
    for root, _, files in os.walk(main_root):
        should_skip = False
        for folder_name in skipped_folders:
            if folder_name.startswith("*"):
                if root.endswith(folder_name[1::]):
                    _[:] = []
                    should_skip = True
                    break

            else:
                element = root.split(os.sep)[-1]
                if element == folder_name:
                    _[:] = []
                    should_skip = True
                    break

        if should_skip:
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


def add_files_content(prompt: str, files_root: dict, title_text: str = None, allowed_files: List = None, skipped_files: List = None):
    for file_name, file_path in files_root.items():
        prompt += title_text.format(file = file_name) + PROMPT_SEPERATOR
        prompt += read_file(file_path, allowed_files = allowed_files, skipped_files = skipped_files) + PROMPT_SEPERATOR

    return prompt

def assemble_for_api(files_root: dict, allowed_files: List = None, skipped_files: List = None):
    api_payload = ""
    api_file_seperator = "\n\n---lum--new--file--"

    for file_name, file_path in files_root.items():
        raw_content = read_file(file_path, allowed_files=allowed_files, skipped_files=skipped_files)
        sanitized_content = sanitize_code(raw_content, file_name)
        api_payload += f"{api_file_seperator}{file_name}\n{sanitized_content}"
    
    #with open("output-test.txt", "w+", encoding = "utf-8") as e: #for debug, to make sure we send everything well !
    #    e.write(api_payload.strip())

    return api_payload.strip()