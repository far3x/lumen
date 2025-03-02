import os
from typing import List


def get_project_structure(root_path: str, skipped_folders: List):
    root_path_name = "".join(root_path.split("/")[-1] + "/")
    print(root_path_name)
    structure = {root_path_name: {}}

    for root, directories, files in os.walk(root_path, topdown = True):
        if any(root.endswith(folder) for folder in skipped_folders):
            directories[:] = []
            structure[root_path_name][root.split("/")[-1]] = {}
            continue

        base = structure[root_path_name]
        level = len(root.split("\\")) - len(root_path.split("\\"))
        print(level, "level")
        for x in range(level, 0, -1):
            folder_subname = root.split("\\")[-x]
            print(root.split("\\"))
            print(folder_subname)
            print(base)
            print(base[folder_subname])
            base = base[folder_subname]

        print(f"BASE IS : {base}")
        print(root_path.split("\\"), 1)
        print(root, "\n", root.split("\\"), 2,  "\n\n")

        #folder_level = len(structure[root_path_name][root.split("/")])

        '''if index == folders_num:
            index = 0
            folder_level += 1
            folders_num = 0'''

        #print(root, directories, files)
        
        #add folders
        #add files
        #iterate through folders
        #add folders and files again until we can't :)
        
        actual_directory = root.split()

        '''if directories:
            files_index += 1
            for directory in directories:
                structure[root_path_name][str({directory}) + "/"] = {}
        
        if files:
            for file in files:
                pass'''
        

    print(structure)

get_project_structure(root_path = "C:/Users/far30/Downloads/GENERATION MEMOIRE TECHNIQUE API", skipped_folders = [".git", "__pycache__"])


"""

WHAT WE WANT:

main_directory/
 ├── dir0/
 |    └── special_file.txt
 ├── dir1/
 |    ├── file2.txt
 |    └── file1.txt
 ├── dir2/
 |    ├── subdir2/
 |    └── subdir1/
 |         ├── file_in_subdir1.txt
 |         └── subsubdir1/
 |              └── deep_file.txt
 ├── empty_dir/
 └── root_file.txt

"""