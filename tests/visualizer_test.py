from ptap import visualizer
import os, json

#we test the json structure of the existing project here
#structure we want https://imgur.com/a/iAjXl0n

#structure ALWAYS starts with files and its in alphabetical order since the algo I made was a bit different
wanted_structrue = {
    "LICENSE": {},
    "README.md": {},
    "requirements.txt": {},
    "setup.py": {},
    ".git/": {},
    "ptap/": {
        "__pycache__/": {},
        "__init__.py": {},
        "assembly.py": {},
        "file_reader.py": {},
        "main.py": {},
        "visualizer.py": {},  
    },
    "__pycache__": {},
    "ptap.egg-info/": {},
    "tests/": {
        "assembly_test.py": {},
        "reader_test.py": {},
        "visualizer_test.py": {}
    }
}


data = json.dumps(
    visualizer.get_project_structure(
        root_path = os.getcwd(), 
        skipped_folders = [ #no need to specify the "/" element, and will show the directory but not the content
            ".git", 
            "__pycache__",
            "ptap.egg-info"
        ]
    ),
    indent = 4,
)

print(data)