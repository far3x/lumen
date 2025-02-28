import os
from typing import List


def get_project_structure(root_path: str, skipped_folders: List):
    structure = []

    for root, directories, files in os.walk(root_path, topdown = True):
        if any(root.endswith(folder) for folder in skipped_folders):
            directories[:] = []
            continue

        print(root, directories, files)

    return structure

get_project_structure("C:/Users/far30/Downloads/GENERATION MEMOIRE TECHNIQUE API", [".git", "__pycache__"])


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