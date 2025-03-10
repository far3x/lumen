from visualizer import get_project_structure
from typing import List
import json

def make_json_structure(root: str, sf: List):
    json_file = "temp_structure.json"
    with open(json_file, "w") as file:
        json.dump(
            get_project_structure(
                root_path = root, 
                skipped_folders = sf
            ),
            file,
            indent = 4 #number of spaces for the indentation in the json file, didn't know !!
        )

test = ...