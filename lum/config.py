import os, json, sys

EXPECTED_CONFIG_KEYS = [
    "intro_text",
    "title_text",
    "skipped_folders",
    "skipped_files",
    "allowed_file_types",
    "use_ai_instructions",
    "ai_instructions_text"
]

BASE_CONFIG = {
    "intro_text":

"""Here is a coding project I am working on.
It starts with the full structure of the project, then you will have each file title and file content.

Respond with 'OK' and for now, just understand the project completely.
I will ask for help in the next prompt so you can assist me with this project.
""",

    "title_text": "--- FILE : {file} ---",

    "use_ai_instructions": False,
    "ai_instructions_text": """Please follow these rules :

- Don't comment the code at all, unless it's specified. If comments are here, keep them, otherwise don't add any yourself, even after alot of messages, this is an important rule.
- Output the entirity of the files that changed after I asked for something, no laziness is allowed, so even if the file is long, output it entirely.
- At the end, always do a paragraph / do points to explain the changes that you did precisely.

Good luck !
""",

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
        "poetry.lock", "composer.lock", "Gemfile.lock", "Cargo.lock", "Podfile.lock", "go.sum",
        ".DS_Store", "Thumbs.db", ".Rhistory", ".node_repl_history", "yarn-debug.log", ".tfstate",
        ".sublime-workspace", ".sublime-project", ".env", ".tfstate.backup", "yarn-error.log",
        "a.out", "main.exe", "celerybeat-schedule", "npm-debug.log", ".eslintcache"
    ],

    "allowed_file_types": [
        ".R", ".ada", ".adb", ".adoc", ".ads", ".asciidoc", ".asm", ".asp", ".aspx", ".ascx",
        ".au3", ".avdl", ".avsc", ".babelrc", ".bash", ".bazel", ".bib", ".browserslistrc", ".c",
        ".cc", ".cfg", ".cg", ".cjs", ".clj", ".cljc", ".cljs", ".cls", ".cmake", ".cmd", ".comp",
        ".conf", ".cpp", ".cs", ".csproj", ".cshtml", ".css", ".dart", ".diff", ".conf", ".ino",
        ".editorconfig", ".edn", ".ejs", ".elm", ".env", ".env.example", ".env.local", ".erl",
        ".eslintrc", ".eslintrc.js", ".eslintrc.json", ".eslintrc.yaml", ".ex", ".exs", ".f",
        ".f90", ".fish", ".for", ".frag", ".fx", ".gd", ".gdshader", ".geom", ".gitattributes",
        ".gitignore", ".gitmodules", ".gitlab-ci.yml", ".glsl", ".gql", ".go", ".graphql",
        ".groovy", ".h", ".haml", ".hbs", ".hh", ".hjson", ".hlsl", ".hpp", ".hrl", ".hs",
        ".htaccess", ".htm", ".html", ".htpasswd", ".inc", ".ini", ".ipynb",
        ".j2", ".java", ".jinja", ".js", ".json", ".json5", ".jsx", ".kt", ".kts", ".less", ".lhs",
        ".liquid", ".lisp", ".log", ".lsp", ".ltx", ".lua", ".m", ".mailmap", ".markdown",
        ".marko", ".md", ".metal", ".mjs", ".mm", ".mustache", ".netlify.toml", ".npmrc",
        ".nvmrc", ".pas", ".patch", ".php", ".pl", ".plist", ".pm", ".pp",
        ".prettierrc", ".prettierrc.js", ".prettierrc.json", ".prettierrc.yaml", ".properties",
        ".proto", ".ps1", ".psd1", ".psm1", ".pug", ".py", ".pyi", ".pylintrc", ".r", ".rb",
        ".rbw", ".rs", ".rst", ".s", ".sass", ".scala", ".scm", ".scss", ".sh",
        ".sln", ".slim", ".soy", ".sql", ".styl", ".sty", ".sv", ".svelte", ".dev",
        ".swift", ".tcl", ".tesc", ".tese", ".tex", ".textile", ".tf", ".tfvars", ".thrift",
        ".toml", ".ts", ".tsx", ".txt", ".twig", ".v", ".vb", ".vbhtml", ".vbproj",
        ".vert", ".vbs", ".vhdl", ".vue", ".vtt", ".wgsl", ".xhtml", ".xml", ".yaml", ".yarnrc",
        ".yml", ".zsh", "BUILD", "CMakeLists.txt", "Cargo.toml", "Dockerfile", "Gemfile",
        "Jenkinsfile", "Makefile", "Pipfile", "Vagrantfile", "WORKSPACE", "bower.json",
        "browserslist", "build.gradle", "build.xml", "composer.json", "docker-compose.yml",
        "now.json", "package.json", "pom.xml", "pyproject.toml", "requirements.txt",
        "rollup.config.js", "setup.py", "tsconfig.json", "vercel.json", "webpack.config.js"
    ]
}

config_folder = ".lum"
config_file = "config.json"

def check_config():
    config_dir, config_path = get_config_directory(), get_config_file()
    config_needs_creation_or_reset, config_data = False, {}

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = json.load(f)

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


def get_config_directory():
    return str(os.path.join(os.path.expanduser("~"), config_folder))

def get_config_file():
    return str(os.path.join(get_config_directory(), config_file))

def get_config_data():
    try:
        with open(get_config_file(), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return BASE_CONFIG.copy()

def save_config_data(data):
    try:
        with open(get_config_file(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Could not save config file: {e}")

def store_pat(pat: str):
    config_data = get_config_data()
    config_data["pat"] = pat
    save_config_data(config_data)

def get_pat():
    return get_config_data().get("pat")

def remove_pat():
    config_data = get_config_data()
    if "pat" in config_data:
        del config_data["pat"]
        save_config_data(config_data)
    return True

def get_intro():
    return get_config_data().get("intro_text", BASE_CONFIG["intro_text"])

def get_title():
    return get_config_data().get("title_text", BASE_CONFIG["title_text"])

def get_skipped_folders():
    return get_config_data().get("skipped_folders", BASE_CONFIG["skipped_folders"])

def get_skipped_files():
    return get_config_data().get("skipped_files", BASE_CONFIG["skipped_files"])

def get_allowed_file_types():
    return get_config_data().get("allowed_file_types", BASE_CONFIG["allowed_file_types"])

def get_use_ai_instructions():
    return get_config_data().get("use_ai_instructions", BASE_CONFIG["use_ai_instructions"])

def get_ai_instructions_text():
    return get_config_data().get("ai_instructions_text", BASE_CONFIG["ai_instructions_text"])