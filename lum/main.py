from lum.visualizer import *
from lum.assembly import *
from lum.config import *
from lum.github import *
from lum.smart_read import *

from typing import List
import json, os, sys, platform, subprocess, argparse, pyperclip

#get parameters initially from file
def get_parameters():
    base_parameters = {
        "intro_text": get_intro(),
        "title_text": get_title(),
        "skipped_folders": get_skipped_folders(),
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


def lum_command(args, isGitHub: bool = False, GitHubRoot: str = None):
    print("Launching...")
    root_path = args.path

    if isGitHub:
        if GitHubRoot:
            root_path = GitHubRoot

        else:
            print("The path to the GitHub repo was not found!")
            sys.exit(1)

    if args.txt: output_file = args.txt
    else: output_file = None

    check_config() #in case of first run, will automatically add config files etc
    base_parameters = get_parameters()

    #used parameters, read ONCE each parameter, no more -> output should be :
    #x2 skipped folders, x2 skipped files, x1 intro, x1 title, x1 allowed file types ---- OBJECTIVE NOT MET BUT ALMOST
    #before : was this but, the higher the folders = more iterations for reading files
    #this is the best time optimization, and was the most consuming process
    #this + not forcing encoding detection = best possible performances (if we dont count python compilers ahah)
    
    #went from reading parameters once every file read, to once BEFORE, now reading files "only" 18 times total
    #this is optimized and stable, wont change unless i really want that ms difference
    #(it won't rly change anything to read 3.5 times more basically !)
    intro_text = base_parameters["intro_text"]

    if gitignore_exists(""): skipped_files, _ = gitignore_skipping() #skipped_folders never used here, maybe can optimize later that
    else: skipped_files = get_files_parameters()["non_allowed_read"]

    allowed_files = get_files_parameters()["allowed_files"]

    skipped_folders = base_parameters["skipped_folders"]

    files_root = get_files_root(root_path, skipped_folders)
    title_text = base_parameters["title_text"]

    #if ranking enabled, use the ranking in backend to show top 20 most consuming files in term of token by default
    if args.leaderboard is not None:
        rank_tokens(files_root, args.leaderboard, allowed_files = allowed_files, skipped_files = skipped_files)


    #STRUCTURE, MOST IMPORTANT FOR PROMPT
    structure = ""
    structure = add_intro(structure, intro_text)
    structure = add_structure(structure, make_structure(root_path, skipped_folders))
    structure = add_files_content(structure, files_root, title_text = title_text, allowed_files = allowed_files, skipped_files = skipped_files)


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
        sys.exit(1)

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
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description = "The best tool to generate AI prompts from code projects, in a single command !"
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
    
    elif args.github: #if github link we go to the repo, parse the link to make it usable for the api call, then take all the files and make an analysis
        lum_github(args = args)

    else: #if not reset or config, main purpose of the script
        lum_command(args = args)
        

if __name__ == "__main__":
    main()