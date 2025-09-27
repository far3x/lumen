from lum.smart_read import read_file
from lum.gitignore import *
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
    analyzed_folder_count = 0
    min_level = 0
    for root, _, files in os.walk(main_root):
        should_skip = False
        
        relative_dir = os.path.relpath(root, main_root)
        
        if any(part.startswith('.') for part in relative_dir.split(os.sep) if part != '.'):
            should_skip = True
        else:
            for folder_pattern in skipped_folders:
                if folder_pattern.startswith("*"):
                    if root.endswith(folder_pattern[1::]):
                        should_skip = True
                        break

                elif '/' in folder_pattern or '\\' in folder_pattern:
                    normalized_pattern = os.path.normpath(folder_pattern)
                    if relative_dir == normalized_pattern or relative_dir.startswith(normalized_pattern + os.sep):
                        should_skip = True
                        break

                else:
                    if os.path.basename(root) == folder_pattern:
                        should_skip = True
                        break

        if should_skip:
            _[:] = []
            continue

        analyzed_folder_count += 1
        if min_level == 0:
            min_level = len(main_root.split(os.sep))

        if files:
            for file in files:
                if file.startswith('.'):
                    continue
                if any(file.endswith(allowed_file) for allowed_file in allowed):
                    file_root = f"{root}{os.sep}{file}"
                    file_list_index = "/".join(file_root.split(os.sep)[min_level::])
                    files_list[file_list_index] = file_root

    return files_list, len(files_list), analyzed_folder_count

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
    from lum.data import sanitize_code

    full_code_blob = ""
    api_file_seperator = "\n\n---lum--new--file--"

    for file_name, file_path in files_root.items():
        raw_content = read_file(file_path, allowed_files=allowed_files, skipped_files=skipped_files)
        full_code_blob += f"{api_file_seperator}{file_name}\n{raw_content}"
    
    sanitized_payload = sanitize_code(full_code_blob)

    return sanitized_payload.strip()