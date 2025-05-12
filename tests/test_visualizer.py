from lum import visualizer
import os, json

#we test the json structure of the existing project here

#structure ALWAYS starts with files and its in alphabetical order since the algo I made was a bit different
#can't rly test the structure here since I'm updating the project way too much, so I just print the output and it should look like this in any os :
#this is the output when we ignore ".git", "lum.egg-info" and "__pycache__" folders

"""
{
    "lumen/": {
        "LICENSE": {},
        "README.md": {},
        "requirements.txt": {},
        "setup.py": {},
        ".git/": {},
        "lum/": {
            "assembly.py": {},
            "file_reader.py": {},
            "main.py": {},
            "visualizer.py": {},
            "__init__.py": {}
        },
        "__pycache__/": {},
        "lum.egg-info/": {},
        "tests/": {
            "assembly_test.py": {},
            "reader_test.py": {},
            "visualizer_test.py": {}
        }
    }
}
"""

#data print above
data = json.dumps( 
    visualizer.get_project_structure(
        root_path = os.getcwd(), 
        skipped_folders = [ #no need to specify the "/" element, and will show the directory but not the content
            ".git", 
            "__pycache__",
            "lum.egg-info"
        ]
    ),
    indent = 4,
)

#print(data)

#output when nothing is ignored :

"""{
    "LUMEN/": {
        "LICENSE": {},
        "README.md": {},
        "requirements.txt": {},
        "setup.py": {},
        "lum/": {
            "assembly.py": {},
            "file_reader.py": {},
            "main.py": {},
            "visualizer.py": {},
            "__init__.py": {},
            "__pycache__/": {
                "assembly.cpython-310.pyc": {},
                "file_reader.cpython-310.pyc": {},
                "visualizer.cpython-310.pyc": {},
                "__init__.cpython-310.pyc": {}
            }
        },
        "lum.egg-info/": {
            "dependency_links.txt": {},
            "entry_points.txt": {},
            "PKG-INFO": {},
            "SOURCES.txt": {},
            "top_level.txt": {}
        },
        "tests/": {
            "assembly_test.py": {},
            "reader_test.py": {},
            "visualizer_test.py": {}
        }
    }
}"""

#data print above
data = json.dumps(
    visualizer.get_project_structure(
        root_path = os.getcwd(), 
        skipped_folders = [ 
            #no need to specify the "/" element, and will show the directory but not the content
        ]
    ),
    indent = 4,
)

#print(data)