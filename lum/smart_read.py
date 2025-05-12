from typing import List
import json, chardet


#skibidi (sorry if u find this)
#will put in config soon
allowed_files = [
    ".py", ".pyi", ".r", ".R", ".php", ".ipynb", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
    ".java", ".kt", ".kts", ".scala", ".groovy", ".c", ".cpp", ".cc", ".h", ".hpp", ".hh",
    ".cs", ".vb", ".go", ".rs", ".rb", ".rbw", ".swift", ".m", ".mm", ".pl", ".pm", ".lua",
    ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less", ".hbs", ".ejs", ".pug",
    ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env", ".md",
    ".markdown", ".rst", "Makefile", ".cmake", ".bazel", "BUILD", "WORKSPACE", ".txt",
    "package.json", "package-lock.json", "yarn.lock", "bower.json", ".babelrc", ".eslintrc",
    ".eslintrc.js", ".eslintrc.json", ".eslintrc.yaml", ".prettierrc", ".prettierrc.js",
    ".prettierrc.json", ".prettierrc.yaml", "webpack.config.js", "rollup.config.js", ".gitignore"
    "requirements.txt", "Pipfile", "Pipfile.lock", "setup.py", "pyproject.toml", ".pylintrc",
    "Gemfile", "Gemfile.lock", "build.gradle", "pom.xml", "tsconfig.json", ".styl", ".twig",
    "composer.json", "composer.lock", "Cargo.toml", "Cargo.lock", ".csv", ".tsv", ".sql", ".gd"
]

#same
non_allowed_read = [
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock",
    "poetry.lock", "composer.lock", "Gemfile.lock", "Cargo.lock", "Podfile.lock",
    ".DS_Store", "Thumbs.db", ".eslintcache", ".Rhistory", ".node_repl_history",
]


def chunk_read(file_path: str, chunk_size: int = 1024):
    while True:
        data = file_path.read(chunk_size)
        if not data:
            break
        yield data


def read_ipynb(file_path: str, cell_seperator: str = None) -> str:
    output_lines = []
    with open(file_path, 'r', encoding='utf-8') as f: #ipynb = utf-8
        data = json.load(f)
    
    for cell in data.get('cells', []):
        cell_type = cell.get('cell_type')
        if cell_type in ['markdown', 'code']:
            output_lines.append("--- CELL ---\n" if not cell_seperator else cell_seperator)
            source_content = cell.get('source', [])
            output_lines.append("".join(source_content) + "\n")
            
    return "\n".join(output_lines)


#auto encoding detection
#can be used as a seperate package (import pylumen / pylumen.detect_encoding(file_path))
def detect_encoding(file_path: str) -> str:
    if file_path.lower().endswith(".md") or file_path.lower().endswith(".txt"):
        #md/txt files hould be set on utf-8
        #chardet detects it as the wrong encoding XD, maybe ill write my own encoding library who knows
        return 'utf-8'
    
    with open(file_path, 'rb') as f:
        sample = f.read(4 * 1024)
        #first 4kb, the less we read the faster
        #this function makes the main function take time to output with a large amount of files :( 
        #(will optimize soon !)
    
    result = chardet.detect(sample)
    encoding = result['encoding']
        
    return 'utf-8' if encoding is None or encoding.lower() == 'ascii' else encoding


def read_file(file_path: str, allowed_files: List = allowed_files):
    if not any(file_path.endswith(allowed_file) for allowed_file in allowed_files):
        return "--- NON READABLE FILE ---"
    
    content = ""
    LARGE_OUTPUT = "--- FILE TOO LARGE / NO NEED TO READ ---"
    ERROR_OUTPUT = "--- ERROR READING FILE ---"
    EMPNR_OUTPUT = "--- EMPTY / NON READABLE FILE ---"

    #ipynb
    if file_path.endswith(".ipynb"):
        try:
            content += read_ipynb(file_path = file_path)
            return content if content else EMPNR_OUTPUT

        except Exception as e:
            print(f"Error while reading the ipynb file : {file_path}. Skipping file. Error: {e}")
            return ERROR_OUTPUT

    #skipped files (large files, module files... etc that are not needed)
    if any(file_path.endswith(dont_read) for dont_read in non_allowed_read):
        return LARGE_OUTPUT
    
    #rest, any allowed file
    try:
        #print("DEBUG - " + detect_encoding(file_path)) #used this to fix readme utf issue, also fixed folders being taken into account that should not :skull:
        with open(file_path, "r", encoding = detect_encoding(file_path = file_path)) as file: #only reading here
            for chunk in chunk_read(file):
                content += chunk
        
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading {file_path}. Skipping file. Error: {e}")
        return ERROR_OUTPUT
    
    return content if content else EMPNR_OUTPUT