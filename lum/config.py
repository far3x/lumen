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
        ".git", ".svn", ".hg", "node_modules", "*.cache", ".*cache", ".*_cache", "_site",
        "__pycache__", "venv", ".venv", "env", "*.egg-info", "*.dist-info", "mkdocs_build",
        ".idea", ".vscode", "nbproject", ".settings", "DerivedData", "coverage", "~*",
        "build", "dist", "out", "output", "target", "bin", "obj", "site", "docs/_build",
        ".angular", ".next/cache", ".nuxt", ".parcel-cache", ".pytest_cache", "log",
        ".mypy_cache", ".ruff_cache", ".tox", "temp", "tmp", "logs", "android/app/build",
        "vendor", "deps", "Pods", "bower_components", "jspm_packages", "web_modules",
        ".svelte-kit", "storage", "bootstrap/cache", "public/build", "public/hot",
        "var", ".serverless", ".terraform", "storybook-static", "ios/Pods", "dump"
    ],

    "skipped_files": [
        "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock", "npm-debug.log*",
        "poetry.lock", "composer.lock", "Gemfile.lock", "Cargo.lock", "Podfile.lock", "go.sum"
        ".DS_Store", "Thumbs.db", ".Rhistory", ".node_repl_history", "yarn-debug.log", ".tfstate",
        ".sublime-workspace", ".sublime-project", ".env", ".tfstate.backup", "yarn-error.log",
        "a.out", "main.exe", "celerybeat-schedule", "npm-debug.log", ".eslintcache"
    ],

    "allowed_file_types": [
        ".R", ".ada", ".adb", ".adoc", ".ads", ".asciidoc", ".asm", ".asp", ".aspx", ".ascx"
        ".au3", ".avdl", ".avsc", ".babelrc", ".bash", ".bazel", ".bib", ".browserslistrc", ".c"
        ".cc", ".cfg", ".cg", ".cjs", ".clj", ".cljc", ".cljs", ".cls", ".cmake", ".cmd", ".comp"
        ".conf", ".cpp", ".cs", ".csproj", ".cshtml", ".css", ".dart", ".diff"
        ".editorconfig", ".edn", ".ejs", ".elm", ".env", ".env.example", ".env.local", ".erl"
        ".eslintrc", ".eslintrc.js", ".eslintrc.json", ".eslintrc.yaml", ".ex", ".exs", ".f"
        ".f90", ".fish", ".for", ".frag", ".fx", ".gd", ".gdshader", ".geom", ".gitattributes"
        ".gitignore", ".gitmodules", ".gitlab-ci.yml", ".glsl", ".gql", ".go", ".graphql"
        ".groovy", ".h", ".haml", ".hbs", ".hh", ".hjson", ".hlsl", ".hpp", ".hrl", ".hs"
        ".htaccess", ".htm", ".html", ".htpasswd", ".inc", ".ini", ".ipynb"
        ".j2", ".java", ".jinja", ".js", ".json", ".json5", ".jsx", ".kt", ".kts", ".less", ".lhs"
        ".liquid", ".lisp", ".log", ".lsp", ".ltx", ".lua", ".m", ".mailmap", ".markdown"
        ".marko", ".md", ".metal", ".mjs", ".mm", ".mustache", ".netlify.toml", ".npmrc"
        ".nvmrc", ".pas", ".patch", ".php", ".pl", ".plist", ".pm", ".pp"
        ".prettierrc", ".prettierrc.js", ".prettierrc.json", ".prettierrc.yaml", ".properties"
        ".proto", ".ps1", ".psd1", ".psm1", ".pug", ".py", ".pyi", ".pylintrc", ".r", ".rb"
        ".rbw", ".rs", ".rst", ".s", ".sass", ".scala", ".scm", ".scss", ".sh"
        ".sln", ".slim", ".soy", ".sql", ".styl", ".sty", ".sv", ".svelte"
        ".swift", ".tcl", ".tesc", ".tese", ".tex", ".textile", ".tf", ".tfvars", ".thrift"
        ".toml", ".ts", ".tsx", ".txt", ".twig", ".v", ".vb", ".vbhtml", ".vbproj"
        ".vert", ".vbs", ".vhdl", ".vue", ".vtt", ".wgsl", ".xhtml", ".xml", ".yaml", ".yarnrc"
        ".yml", ".zsh", "BUILD", "CMakeLists.txt", "Cargo.toml", "Dockerfile", "Gemfile"
        "Jenkinsfile", "Makefile", "Pipfile", "Vagrantfile", "WORKSPACE", "bower.json"
        "browserslist", "build.gradle", "build.xml", "composer.json", "docker-compose.yml"
        "now.json", "package.json", "pom.xml", "pyproject.toml", "requirements.txt"
        "rollup.config.js", "setup.py", "tsconfig.json", "vercel.json", "webpack.config.js"
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