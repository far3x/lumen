from lum.visualizer import *
from lum.assembly import *
from lum.config import *
from lum.github import *
from lum.smart_read import *

from typing import List
import json, os, platform, subprocess, argparse, pyperclip

#get parameters initially from file
def get_parameters():
    base_parameters = {
        "intro_text": get_intro(),
        "title_text": get_title(),
        "skipped_folders": get_skipped_folders(), #more soon
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


################################
# MEOW XD sorry if u read this #
################################


def lum_command(args, isGitHub: bool = False, GitHubRoot: str = None):
    print("Launching...")
    root_path = args.path
    if isGitHub:
        if GitHubRoot:
            root_path = GitHubRoot
        else:
            print("The path to the GitHub repo was not found!")
            exit()

    if args.txt:
        output_file = args.txt
    else:
        output_file = None

    check_config() #in case of first run, will automatically add config files etc
    base_parameters = get_parameters()


    files_root = get_files_root(root_path, base_parameters["skipped_folders"])


    #if ranking enabled, use the ranking in backend to show top 20 most consuming files in term of token by default
    if args.leaderboard is not None:
        rank_tokens(files_root, args.leaderboard)


    #STRUCTURE, MOST IMPORTANT FOR PROMPT
    structure = ""
    structure = add_intro(structure, base_parameters["intro_text"])
    structure = add_structure(structure, make_structure(root_path, get_parameters()["skipped_folders"]))
    structure = add_files_content(structure, files_root, title_text = base_parameters["title_text"])


    if output_file is None:
        try:
            pyperclip.copy(structure)
            print("Prompt copied to clipboard.\nIf you encounter a very big codebase, try to get a '.txt' output for better performances (clipboard won't make your pc lag).")
        #non-windows case, where the clipboard won't work on all containers because of some limitations. will try to find a LIGHT advanced fix asap (tkinter is a possibility but too large for a single module where we just need clipboard support)
        except pyperclip.PyperclipException as e:
            try:
                with open("prompt.txt", "w+", encoding="utf-8") as file:
                    file.write(structure)
                print("Copy to clipboard failed. Output is done in the root, as 'prompt.txt', to fix this please look at the README documentation (2 commands to fix this for most linux cases, install xsel or xclip).")
            except Exception as e:
                print(f"Error saving prompt to file {output_path}: {e}")

    elif output_file is not None:
        output_path = os.path.join(root_path, f"{output_file}.txt")
        try:
            with open(output_path, "w+", encoding="utf-8") as file:
                file.write(structure)
            print(f"Prompt saved to {output_path}")
        except Exception as e:
            print(f"Error saving prompt to file {output_path}: {e}")


def lum_github(args):
    git_exists = check_git()
    if git_exists == False:
        exit()

    github_link = args.github
    check_repo(github_link)

    if github_link:
        try:
            git_root = download_repo(github_link)
            lum_command(args = args, isGitHub = True, GitHubRoot = git_root)
        finally:
            git_root_to_remove = os.path.join(get_config_directory(), github_link.split("/")[-1].replace(".git", ""))
            if not git_root_to_remove:
                 git_root_to_remove = os.path.join(get_config_directory(), github_link.split("/")[-2])
            remove_repo(git_root_to_remove)
    else:
        print("GitHub repo doesn't exist, please try again with a correct link (check that the repository is NOT private, and that you are connected to internet !)")
        exit()


def main():
    parser = argparse.ArgumentParser(
        description = "The best tool to generate AI prompts from code projects and make any AI understand a whole project!"
    )

    parser.add_argument(
        "path",
        nargs = "?", #0 or 1 argument #HOW GOOD IS ARGPARSE LET THEM COOK, WHOEVER MADE THIS IS A GENIUS
        default = os.getcwd(),
        help = "Path to the root to process. If not specified, will use the main root.",
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

    parser.add_argument( #no more hide, hiding prompt parts is useless
        "-l",
        "--leaderboard",
        nargs = "?",
        const = 20,
        default = None,
        type = int,
        metavar = "NUM", #will show top 20 most consuming files in term of tokens by default, can put any number tho and will show the leaderboard
        help = "Leaderboard of the most token consuming files (default: 20)."
    )

    parser.add_argument(
        "-t",
        "--txt",
        metavar = "FILENAME",
        help = "Outputs the file name as FILENAME.txt in the root."
    )

    parser.add_argument(
        "-g",
        "--github",
        metavar = "REPO",
        help = "Runs the main command into a GitHub repository."
    )

    args = parser.parse_args()

    if args.configure:
        print("Config file opened. Check your code editor.")
        check_config()
        change_parameters()

    elif args.reset:
        check_config()
        reset_config()
    
    #idea for github import would be to git clone the project locally in lum folder, then run the command there, then remove the downloaded folder.
    elif args.github: #if github link we go to this repo, take all the files and make an analysis
        lum_github(args = args)

    else: #if not reset or config, main purpose of the script
        lum_command(args = args)
        

if __name__ == "__main__":
    main()