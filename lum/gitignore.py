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

        #non readable / useless lines
        if not line: continue
        if line.startswith("#"): continue
        if line.startswith("!"): continue

        if line.endswith("/") or line.endswith("\\"):
            #no longer use os.path.basename
            folder_name = line.rstrip('/\\')
            
            if folder_name and folder_name != "." and folder_name != "..":
                skipped_folders.append(folder_name)

        else:
            if line != "." and line != "..":
                 skipped_files.append(line)
    
    return skipped_files, skipped_folders


def gitignore_skipping():
    #get skipped file and folders
    skipped_files, skipped_folders = get_skipped_files(), get_skipped_folders()
    #seperate gitignore into 2 ways -> files / folders
    skipped_files_git, skipped_folders_git = gitignore_read("")

    #merging between existing config + gitignore
    skipped_files = list(set(skipped_files + skipped_files_git))
    skipped_folders = list(set(skipped_folders + skipped_folders_git))

    #return list of skipped files + gitignore ones / skipped folders + gitignore ones
    return skipped_files, skipped_folders