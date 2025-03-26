from ptap.visualizer import *
from ptap.assembly import *
from ptap.config import *
from ptap.github import *

from typing import List
import json, os, platform, subprocess, argparse, pyperclip

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
#    parsing part, hardest part i guess    #
#                                          #
############################################

def ptap_command(args, isGitHub: bool = False, GitHubRoot: str = None):
    print("Launching...")
    root_path = args.path
    if isGitHub:
        if GitHubRoot:
            root_path = GitHubRoot
        else:
            print("The path to the GitHub repo was not found!")
            exit()
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
    
    print("Done ! Paste your prompt into an AI, or open your text folder to get the output.")

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

    parser.add_argument(
        "-g",
        "--github",
        metavar = "GitHub Repo Link",
        help = "Give a structured output from an existing GitHub repo"
    )

    args = parser.parse_args()

    if args.configure:
        print("Config file opened. Check your code editor.")
        check_config()
        change_parameters()

    elif args.reset:
        check_config()
        reset_config()
    
    #idea for github import would be to git clone the project locally in ptap folder, then run the command there, then remove the downloaded folder.
    elif args.github: #if github link we go to this repo, take all the files and make an analysis
        git_exists = check_git()
        if git_exists == False:
            exit()

        github_link = args.github

        check_repo(github_link)
        if github_link:
            git_root = download_repo(github_link)
            ptap_command(args = args, isGitHub = True, GitHubRoot = git_root)
            remove_repo(git_root)
        else:
            print("GitHub repo doesn't exist, please try again with a correct link (check that the repository is NOT private, and that you are connected to internet !)")
            exit()
        

    else: #if not reset or config, main purpose of the script
        ptap_command(args = args)
        

if __name__ == "__main__":
    main()