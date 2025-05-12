from typing import List
from lum.config import *
import json, chardet, tiktoken


#skibidi (sorry if u find this)

def get_files_parameters():
    base_parameters = {
        "allowed_files": get_allowed_file_types(),
        "non_allowed_read": get_skipped_files()
    }
    return base_parameters


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


def rank_tokens(files_root: dict, top: int):
    encoding = tiktoken.get_encoding("cl100k_base")
    token_counts = []

    print("\nCalculating token counts...")

    for file_name, file_path in files_root.items():
        content = read_file(file_path)

        try:
            tokens = encoding.encode(content)
            token_count = len(tokens)
            token_counts.append((token_count, file_name))
        except Exception as e:
            print(f"Error encoding file {file_name}: {e}")

    token_counts.sort(key=lambda item: item[0], reverse=True)

    print(f"\nTop {min(top, len(token_counts))} Most Token-Consuming Files :")

    if not token_counts:
        print("No readable files found to rank.")
    else:
        for i, (count, name) in enumerate(token_counts[:top]):
            print(f"{i + 1}. {name}: {count} tokens")


def read_file(file_path: str, allowed_files: List = None):
    if allowed_files is None:
        allowed_files = get_files_parameters()["allowed_files"]

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
    if any(file_path.endswith(dont_read) for dont_read in get_files_parameters()["non_allowed_read"]):
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