from typing import List

#will put in config asap
allowed_files = [
    ".py", ".pyi",
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
    ".java", ".kt", ".kts", ".scala", ".groovy",
    ".c", ".cpp", ".cc",
    ".h", ".hpp", ".hh",
    ".cs", ".vb",
    ".go",
    ".rs",
    ".rb", ".rbw",
    ".swift", ".m", ".mm",
    ".pl", ".pm",
    ".lua",
    ".r", ".R",
    ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less", ".styl",
    ".hbs", ".ejs", ".pug", ".twig",
    ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env",
    ".md", ".markdown", ".rst", ".txt",
    "Makefile", ".cmake", ".bazel", "BUILD", "WORKSPACE",
    "package.json", "package-lock.json", "yarn.lock", "bower.json",
    ".babelrc", ".eslintrc", ".eslintrc.js", ".eslintrc.json", ".eslintrc.yaml",
    ".prettierrc", ".prettierrc.js", ".prettierrc.json", ".prettierrc.yaml",
    "webpack.config.js", "rollup.config.js", "tsconfig.json",
    "requirements.txt", "Pipfile", "Pipfile.lock", "setup.py", "pyproject.toml", ".pylintrc",
    "Gemfile", "Gemfile.lock",
    "build.gradle", "pom.xml",
    "composer.json", "composer.lock",
    "Cargo.toml", "Cargo.lock",
    ".csv", ".tsv",
    ".sql",
    ".gd"
]

non_allowed_read = [
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Pipfile.lock",
    "poetry.lock",
    "composer.lock",
    "Gemfile.lock",
    "Cargo.lock",
    "Podfile.lock",
    ".DS_Store",
    "Thumbs.db",
    ".eslintcache",
    ".Rhistory",
    ".node_repl_history",
]

#maybe change reading system since chunk read will not be triggered mostly, unless really big file
def chunk_read(file_path: str, chunk_size: int = 1024):
    while True:
        data = file_path.read(chunk_size)
        if not data:
            break
        yield data

def read_file(file_path: str, allowed_files: List = allowed_files):
    if any(file_path.endswith(allowed_file) for allowed_file in allowed_files):
        content = ""
        if any(file_path.endswith(dont_read) for dont_read in non_allowed_read):
            return "--- FILE TOO LARGE / NO NEED TO READ ---"
        with open(file_path, "r", encoding = "utf-8") as file: #only reading here
            for chunk in chunk_read(file):
                content += chunk
        file.close()
        if content == "":
            return "--- EMPTY/NON READABLE FILE ---"
        return content