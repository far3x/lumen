#objective here is to ignore files mentionned in gitignore
#need to check if the gitignore is well formatted first
#take existing configuration, then add gitignore files / folders
#all have a different formatting tho, need to work on that

import os
from typing import List
from lum.config import * #to get config (to skip folders and files)


def gitignore_exists(root: str):
    path = os.path.join(root, ".gitignore")
    return os.path.exists(path = path)


def gitignore_read(root: str):
    path = os.path.join(root, ".gitignore")
    skipped_files, skipped_folders = [], []

    #in case exception here, even tho this exception should NEVER trigger since the function only triggers when a gitignore is found
    try:
        with open(path, "r") as d:
            lines = d.readlines()
    except Exception as e:
        print(f"Error : {e}.")
        return skipped_files, skipped_folders
    
    for line_raw in lines:
        #remove "\n" from line on each line's end
        line = line_raw.strip()
        #print(line)

        #non readable / useless lines
        if not line: continue
        if line.startswith("#"): continue
        if line.startswith("!"): continue

        if line.endswith("/") or line.endswith("\\"):
            normalized_path_for_basename = line.rstrip('/\\')
            if not normalized_path_for_basename: continue
            folder_name = os.path.basename(os.path.normpath(normalized_path_for_basename))
            
            if folder_name and folder_name != "." and folder_name != "..":
                skipped_folders.append(folder_name)
        else:
            if line != "." and line != "..":
                 skipped_files.append(line)
    
    #print(skipped_files, skipped_folders) #works well
    return skipped_files, skipped_folders


def gitignore_skipping():
    #get skipped file and folders
    skipped_files, skipped_folders = get_skipped_files(), get_skipped_folders()
    #print(skipped_files, skipped_folders)
    #seperate gitignore into 2 ways -> files / folders
    skipped_files_git, skipped_folders_git = gitignore_read("")

    #merging between existing config + gitignore
    skipped_files = list(set(skipped_files + skipped_files_git))
    #print("1 - ", skipped_files) #debug
    skipped_folders = list(set(skipped_folders + skipped_folders_git))
    #print("2 - ", skipped_folders) #debug

    #return list of skipped files + gitignore ones / skipped folders + gitignore ones
    return skipped_files, skipped_folders