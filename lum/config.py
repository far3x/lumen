#Generating a json file in appdata or where the pip module is stocked.
#1 backup version, for when the user wants to reset
#1 base version, so the one the user will use, with customized title, prompt or anything

#all the project SHOULD BE os proof, if you notice something is not OS proof, please create an issue :)

import os, json, sys


EXPECTED_CONFIG_KEYS = [
    "intro_text",
    "title_text",
    "skipped_folders",
    "skipped_files",
    "allowed_file_types"
]

BASE_CONFIG = {
    "intro_text":

"""Here is a coding project I am working on.
It starts with the full structure of the project, then you will have each file title and file content.

Respond with 'OK' and for now, just understand the project completely.
I will ask for help in the next prompt so you can assist me with this project.
""",

    "title_text": "--- FILE : {file} ---", #{file} will be replaced by the file name, KEEP IT PLEASE

    "skipped_folders": [
        ".git", "__pycache__", "node_modules", "venv", ".venv", ".svn", ".hg", "obj", "bin",
        "build", "dist", "target", ".gradle", ".idea", ".vscode", ".egg-info", ".dist-info",
        "logs", "log", "tmp", "temp", ".pytest_cache", ".mypy_cache", ".cache", "vendor",
        "deps", ".next", ".nuxt", ".svelte-kit", ".angular", "coverage", "site", "_site",
        ".sass-cache", "bower_components", "jspm_packages", "web_modules", ".pyc", ".pyo",
        ".swp", ".swo", "~", ".DS_Store", "Thumbs.db", "DerivedData", ".settings", ".classpath",
        ".project", "nbproject", ".sublime-workspace", ".sublime-project", ".terraform",
        ".tfstate", ".tfstate.backup", ".serverless", ".parcel-cache", "storage/framework",
        "storage/logs", "bootstrap/cache", "public/build", "public/hot", "public/storage", "var"
    ],

    "skipped_files": [
        "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock",
        "poetry.lock", "composer.lock", "Gemfile.lock", "Cargo.lock", "Podfile.lock",
        ".DS_Store", "Thumbs.db", ".eslintcache", ".Rhistory", ".node_repl_history",
    ],

    "allowed_file_types": [
        ".py", ".pyi", ".r", ".R", ".php", ".ipynb", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
        ".java", ".kt", ".kts", ".scala", ".groovy", ".c", ".cpp", ".cc", ".h", ".hpp", ".hh",
        ".cs", ".vb", ".go", ".rs", ".rb", ".rbw", ".swift", ".m", ".mm", ".pl", ".pm", ".lua",
        ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less", ".hbs", ".ejs", ".pug",
        ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env", ".md",
        ".markdown", ".rst", "Makefile", ".cmake", ".bazel", "BUILD", "WORKSPACE", ".txt", ".gd",
        "package.json", "package-lock.json", "yarn.lock", "bower.json", ".babelrc", ".eslintrc",
        ".eslintrc.js", ".eslintrc.json", ".eslintrc.yaml", ".prettierrc", ".prettierrc.js",
        ".prettierrc.json", ".prettierrc.yaml", "webpack.config.js", "rollup.config.js", ".gitignore"
        "requirements.txt", "Pipfile", "Pipfile.lock", "setup.py", "pyproject.toml", ".pylintrc",
        "Gemfile", "Gemfile.lock", "build.gradle", "pom.xml", "tsconfig.json", ".styl", ".twig",
        "composer.json", "composer.lock", "Cargo.toml", "Cargo.lock", ".csv", ".tsv", ".sql"
    ]
}


config_folder = ".lum"
config_file = "config.json"

#check if config exists, if not it creates it, otherwise will never change the parameters in case of pip update
#folder check then file check, need to run this on main on every command start


#config files management
#if config folder or file doesnt exist, create it, same if config file is outdated, auto reset
def check_config():
    config_dir, config_path = get_config_directory(), get_config_file()
    config_needs_creation_or_reset, config_data = False, {}

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = json.load(f)

            #check if any expected key is missing
            if not all(key in config_data for key in EXPECTED_CONFIG_KEYS):
                config_needs_creation_or_reset = True

        except Exception as e:
            config_needs_creation_or_reset = True

    else:
        config_needs_creation_or_reset = True

    if config_needs_creation_or_reset:
        try:
            with open(config_path, "w", encoding="utf-8") as config_file:
                json.dump(
                    BASE_CONFIG,
                    fp = config_file,
                    indent = 4
                )
            if not os.path.exists(config_path) or (os.path.exists(config_path) and not config_data):
                print("Configuration files initialized.")

        except Exception as error:
            print(f"Config file not found or could not be modified - error : {error}")
            sys.exit(1)


def reset_config():
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
        print(f"Config file not found or could not be modified - error : {error}")
        sys.exit(1)


#get directories and files for config initialization or reading
def get_config_directory():
    return str(os.path.join(os.path.expanduser("~"), config_folder))

def get_config_file():
    return str(os.path.join(get_config_directory(), config_file))


def get_intro():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["intro_text"]
    data.close()
    return d

def get_title():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["title_text"]
    data.close()
    return d

def get_skipped_folders():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["skipped_folders"]
    data.close()
    return d

def get_skipped_files():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["skipped_files"]
    data.close()
    return d

def get_allowed_file_types():
    with open(get_config_file(), "r") as data:
        d = json.load(data)
        d = d["allowed_file_types"]
    data.close()
    return d