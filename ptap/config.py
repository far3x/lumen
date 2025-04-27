#Generating a json file in appdata or where the pip module is stocked.
#1 backup version, for when the user wants to reset
#1 base version, so the one the user will use, with customized title, prompt or anything

#all the project SHOULD BE os proof, if you notice something is not OS proof, please create an issue :)

import os, json

BASE_CONFIG = {
    "intro_text": """Here is a coding project I am working on.
It starts with the full structure of the project, then you will have each file title and file content.

Respond with 'OK' and for now, and just understand the project completely.
I will ask for help in the next prompt so you can assist me with this project.
""",
    "show_intro": True,
    "title_text": "File : {file}", #{file} will be replaced by the file name, KEEP IT PLEASE
    "show_title": True,
    "skipped_folders": [
        ".git",
        "__pycache__",
        "node_modules",
        "venv",
        ".venv",
        ".svn",
        ".hg",
        "obj",
        "bin",
        "build",
        "dist",
        "target",
        ".gradle",
        ".idea",
        ".vscode",
        "*.egg-info",
        "*.dist-info",
        "logs",
        "log",
        "tmp",
        "temp",
        ".pytest_cache",
        ".mypy_cache",
        ".cache",
        "vendor",
        "deps",
        ".next",
        ".nuxt",
        ".svelte-kit",
        ".angular",
        "coverage",
        "site",
        "_site",
        ".sass-cache",
        "bower_components",
        "jspm_packages",
        "web_modules",
        "*.pyc",
        "*.pyo",
        "*.swp",
        "*.swo",
        "*~",
        ".DS_Store",
        "Thumbs.db",
        "DerivedData",
        ".settings",
        ".classpath",
        ".project",
        "nbproject",
        "*.sublime-workspace",
        "*.sublime-project",
        ".terraform",
        "*.tfstate",
        "*.tfstate.backup",
        ".serverless",
        ".parcel-cache",
        "storage/framework",
        "storage/logs",
        "bootstrap/cache",
        "public/build",
        "public/hot",
        "public/storage",
        "var"
    ]
}


config_folder = ".ptap"
config_file = "config.json"

#check if config exists, if not it creates it, otherwise will never change the parameters in case of pip update
#folder check then file check, need to run this on main on every command start


#config files management

def check_config():
    #make the config directory if doesn't exit in base user path
    if not os.path.exists(get_config_directory()):
        os.makedirs(get_config_directory())

    #same than above but with file configuration
    try: 
        with open(get_config_file(), "r"): 
            pass
            #do nothing if file exists

    except FileNotFoundError:
        with open(get_config_file(), "w+") as config_file:
            json.dump(
                BASE_CONFIG,
                fp = config_file,
                indent = 4
            )
        print("Configuration files initialized")
        config_file.close()

    except Exception as error: 
        print(f"Exception when file read : {error}")
        exit()

def reset_config():
    check_config() #in case user resets config for no reason before he uses ptap command normally, wont create conflicts
    try:
        with open(get_config_file(), "w+") as config_file:
            json.dump(
                BASE_CONFIG,
                fp = config_file,
                indent = 4
            )
            print("Json config file reset")
        config_file.close()
    
    except Exception as error:
        print(f"Exception when file read : {error}")
        exit()


#get directories and files for config initialization or reading

def get_config_directory():
    return str(os.path.join(os.path.expanduser("~"), config_folder))

def get_config_file():
    return str(os.path.join(get_config_directory(), config_file))


#get config infos

#part to redo, very repetitive and useless but works
def get_intro():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["intro_text"]
    data.close()
    return d

def get_intro_status():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["show_intro"]
    data.close()
    return d

def get_title():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["title_text"]
    data.close()
    return d

def get_title_status():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["show_title"]
    data.close()
    return d

def get_skipped_folders():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["skipped_folders"]
    data.close()
    return d