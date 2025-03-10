from typing import List

allowed_files = [
    # Core Programming Languages (Source Code Only)
    ".py", ".ipynb", ".pyi",  # Python
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",  # JavaScript/TypeScript
    ".java", ".kt", ".kts", ".scala", ".groovy",  # Java/Kotlin/Scala/Groovy
    ".c", ".cpp", ".cc",  # C/C++ Source
    ".h", ".hpp", ".hh",  # C/C++ Headers
    ".cs", ".vb",  # C#, Visual Basic
    ".go",  # Go
    ".rs",  # Rust
    ".rb", ".rbw",  # Ruby
    ".swift", ".m", ".mm",  # Swift/Objective-C
    ".pl", ".pm",  # Perl
    ".lua",  # Lua
    ".r", ".R",  # R

    # Web Development
    ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less", ".styl",  # HTML/CSS
    ".hbs", ".ejs", ".pug", ".twig",  # Templating
    ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env", # Configuration

    # Documentation
    ".md", ".markdown", ".rst", ".txt",  # Markdown and Text

    # Build Tools and Package Management (Configuration Files)
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

    # Data Science
    ".csv", ".tsv", ".parquet", ".feather", ".h5", ".hdf5", ".onnx", ".pb",

    # SQL
     ".sql",

     #Godot
     ".gd"
]

def chunk_read(file_path: str, chunk_size: int = 1024):
    while True:
        data = file_path.read(chunk_size)
        if not data:
            break
        yield data

def read_file(file_path: str, allowed_files: List = allowed_files):
    if any(file_path.endswith(allowed_file) for allowed_file in allowed_files):
        content = str()
        with open(file_path, "r", encoding = "utf-8") as file: #only reading here
            for chunk in chunk_read(file):
                content += chunk
        return content