from ptap.visualizer import *
from ptap.assembly import *
from ptap.config import *

from typing import List
import json, os, platform, subprocess, argparse, pyperclip

"""
Idea : 

You're in the terminal, you type "ptap" only, it shows the full structure of the actual directory you're in with the settings you have, or base settings if you didn't change anything
So a structured prompt with the path structure in a json format, then each file title and file content, spaced correctly

Options :
 CLI  DONE - give the path manually if you're not directly in the correct directory
 CLI  DONE - change config file (stocked in pc memory) with "ptap -c"
 CLI  DONE - specify the output (base case = will be in clipboard), but would be able to generate a .txt in the selected folder to be able to change some content in the file manually
 CLI  DONE - reset settings "ptap -r" would reset everything
 CLI  DONE - TO IMPROVE IN FUTURE - not include or hide file intro, structure, or whatever "ptap -h intro" or "ptap -h intro,structure,title"

After each pip update, keep the settings so the user would not lose any content that was changed like title, intro etc
This might change, so look at the documentation to understand the module. (That's draft basically)
"""



#when the user types ptap, initializes check_config() then we add all options like in the file base


#get parameters initially from file
def get_parameters():
    base_parameters = {
        "intro_text": get_intro(),
        "show_intro": get_intro_status(),
        "title_text": get_title(),
        "show_title": get_title_status(),
        "skipped_folders": get_skipped_folders()
    }
    return base_parameters


#all changing parameters

def change_parameters():
    if platform.system() == "Windows":
        os.startfile(get_config_file())

    elif platform.system() == "Darwin":
        subprocess.Popen(["open", get_config_file()])

    else:
        subprocess.Popen(["xdg-open", get_config_file()])


def make_structure(path: str, skipped: List):
    #when user types a path, we use this function with an argument, otherwise no argument and get automatically the path
    data = json.dumps( 
        get_project_structure(
            root_path = path, 
            skipped_folders = skipped
        ),
        indent = 4,
    )

    return data


############################################
#                                          #
#     parsing part, hardest part maybe     #
#                                          #
############################################

def main():
    parser = argparse.ArgumentParser(
        description = "The best tool to generate AI prompts from code projects and make any AI understand a whole project!"
    )

    parser.add_argument(
        "path",
        nargs = "?", #0 or 1 argument #HOW GOOD IS ARGPARSE LET THEM COOK, WHOEVER MADE THIS IS A GENIUS
        default = os.getcwd(),
        help = "Path to the root to process. If not specified, will use the main root on the client.",
    )

    parser.add_argument(
        "-c",
        "--configure",
        action = "store_true", #basically will trigger true when parameter is used, no args in this case
        help = "Opens and allows changing the configuration file."
    )

    parser.add_argument(
        "-r",
        "--reset",
        action = "store_true", #same as -c
        help = "Resets all configurations to default values."
    )

    parser.add_argument( #done
        "-hd",
        "--hide",
        metavar = "Element/Elements", #in help section will show elements instead of "HIDE"
        help = "Hide elements manually like the intro (introdution text in the beginning of the prompt) or the title (will hide the names of each file, NOT RECOMMENDED IT WILL MOST LIKELY MAKE THE AI NOT UNDERSTAND) (seperate with commas, for example : 'ptap -hd intro, title')"
    )

    parser.add_argument( #done
        "-t",
        "--txt",
        metavar = "FileName",
        help = "Specify the output file name (in a .txt file that will be in the root. If you don't use this argument, your content will be copied in your clipboard. For example, 'ptap -t prompt' will generate a file named 'prompt.txt' with the whole project in a structured prompt."
    )

    args = parser.parse_args()

    if args.configure:
        print("Config file opened. Check your code editor.")
        check_config()
        change_parameters()

    elif args.reset:
        check_config()
        reset_config()

    else: #if not reset or config, main purpose of the script
        root_path = args.path
        hidden_elements = []

        if args.txt:
            output_file = args.txt
        else:
            output_file = None
    
        check_config() #in case of first run, will automatically add config files etc
        base_parameters = get_parameters()

        if args.hide:
            hidden_elements = [element.strip() for element in args.hide.split(",")] #hidden elements into list that will be replaced
    
        if "intro" in hidden_elements:
            print("did")
            base_parameters["show_intro"] = False
        
        if "title" in hidden_elements:
            base_parameters["show_title"] = False


        #STRUCTURE, MOST IMPORTANT FOR PROMPT
        structure = ""
        if base_parameters["show_intro"]:
            structure = add_intro(structure, base_parameters["intro_text"])

        structure = add_structure(structure, make_structure(root_path, get_parameters()["skipped_folders"]))

        show_title = True
        if bool(base_parameters["show_title"]) == False:
            show_title = False
        
        files_root = get_files_root(root_path, base_parameters["skipped_folders"])
        structure = add_files_content(structure, files_root, show_title, title_text = base_parameters["title_text"])

        if output_file is None:
            pyperclip.copy(structure)

        elif output_file is not None:
            with open(f"{root_path}/{output_file}.txt", "w+") as file:
                file.write(structure)
            file.close()

if __name__ == "__main__":
    main()