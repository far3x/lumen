from lum.visualizer import *
from lum.assembly import *
from lum.config import *
from lum.smart_read import *

from typing import List
import json, os, sys, platform, subprocess, argparse, pyperclip
from colorama import init, Fore, Style

init(autoreset=True)

def get_parameters():
    base_parameters = {
        "intro_text": get_intro(),
        "title_text": get_title(),
        "skipped_folders": get_skipped_folders(),
    }
    return base_parameters

def change_parameters():
    if platform.system() == "Windows":
        os.startfile(get_config_file())
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", get_config_file()])
    else:
        subprocess.Popen(["xdg-open", get_config_file()])

def make_structure(path: str, skipped: List):
    data = json.dumps(
        get_project_structure(
            root_path = path,
            skipped_folders = skipped
        ),
        indent = 4,
    )
    return data

def lum_command_local(args):
    print("Launching local analysis...")
    root_path = args.path

    if args.txt: output_file = args.txt
    else: output_file = None

    check_config()
    base_parameters = get_parameters()

    config_data = get_config_data()
    use_ai_instructions = config_data.get("use_ai_instructions", False)
    ai_instructions_text = config_data.get("ai_instructions_text", "")
    intro_text = base_parameters["intro_text"]
    if use_ai_instructions and ai_instructions_text:
        intro_text += "\n\nPlease read and remember the special instructions in `ai-instructions.txt` before proceeding."

    if gitignore_exists(""): skipped_files, _ = gitignore_skipping()
    else: skipped_files = get_files_parameters()["non_allowed_read"]

    allowed_files = get_files_parameters()["allowed_files"]
    skipped_folders = base_parameters["skipped_folders"]

    files_root = get_files_root(root_path, skipped_folders)
    title_text = base_parameters["title_text"]

    if args.leaderboard is not None:
        rank_tokens(files_root, args.leaderboard, allowed_files = allowed_files, skipped_files = skipped_files)

    structure = ""
    structure = add_intro(structure, intro_text)

    json_structure_str = make_structure(root_path, skipped_folders)
    if use_ai_instructions and ai_instructions_text:
        try:
            json_structure = json.loads(json_structure_str)
            root_key = next(iter(json_structure))
            json_structure[root_key]["ai-instructions.txt"] = {}
            json_structure_str = json.dumps(json_structure, indent=4)
        except (json.JSONDecodeError, StopIteration):
            pass 
    
    structure = add_structure(structure, json_structure_str)

    if use_ai_instructions and ai_instructions_text:
        structure += title_text.format(file="ai-instructions.txt") + PROMPT_SEPERATOR
        structure += ai_instructions_text + PROMPT_SEPERATOR

    structure = add_files_content(structure, files_root, title_text = title_text, allowed_files = allowed_files, skipped_files = skipped_files)
    
    try:
        import tiktoken
        encoding = tiktoken.get_encoding("cl100k_base")
        token_count = len(encoding.encode(structure))
        print(f"Estimated prompt token count: {Fore.CYAN}{token_count}")
    except Exception:
        print(f"{Fore.YELLOW}Could not calculate token count.")

    if output_file is None:
        try:
            pyperclip.copy(structure)
            print(Fore.GREEN + "Prompt copied to clipboard.")
            print(Style.DIM + "If you encounter a very big codebase, try to get a '.txt' output for better performances.")
        except pyperclip.PyperclipException as e:
            output_path = os.path.join(os.getcwd(), "prompt.txt")
            try:
                with open(output_path, "w+", encoding="utf-8") as file:
                    file.write(structure)
                print(Fore.YELLOW + f"Copy to clipboard failed. Output saved to '{output_path}'.")
                print(Style.DIM + "To fix clipboard issues on Linux, install xsel or xclip.")
            except Exception as e:
                print(Fore.RED + f"Error saving prompt to file {output_path}: {e}")

    elif output_file is not None:
        output_path = os.path.join(root_path, f"{output_file}.txt")
        try:
            with open(output_path, "w+", encoding="utf-8") as file:
                file.write(structure)
            print(Fore.GREEN + f"Prompt saved to {output_path}")
        except Exception as e:
            print(Fore.RED + f"Error saving prompt to file {output_path}: {e}")

def lum_github(args):
    from lum.github import check_git, check_repo, download_repo, remove_repo 

    git_exists = check_git()
    if not git_exists:
        sys.exit(1)

    github_link = args.github
    if not check_repo(github_link):
        print(Fore.RED + "GitHub repo doesn't exist or is private. Please try again with a correct public link.")
        sys.exit(1)

    try:
        git_root = download_repo(github_link)
        args.path = git_root
        lum_command_local(args)

    finally:
        git_root_to_remove = os.path.join(get_config_directory(), github_link.split("/")[-1].replace(".git", ""))
        remove_repo(git_root_to_remove)

def lum_login(args):
    import lum.api as api

    if get_pat():
        print(Fore.YELLOW + "You are already logged in.")
        print("To switch accounts, please run `lum logout` first.")
        return

    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Lumen Contributor Network!" + Style.RESET_ALL)
    print("To authorize this device, you must agree to the following:")
    print(f"  {Fore.YELLOW}1.{Style.RESET_ALL} You agree to our Terms of Service and Contributor License Agreement.")
    print(f"     {Style.DIM}You can review them at lumen.onl/docs/legal{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}2.{Style.RESET_ALL} You confirm the code you contribute is your own original work.")
    print(f"  {Fore.YELLOW}3.{Style.RESET_ALL} You understand that all code is sanitized {Fore.GREEN+Style.BRIGHT}LOCALLY{Style.RESET_ALL} on your machine.")
    print(f"     {Style.DIM}Your raw code, secrets, and IP are never transmitted.{Style.RESET_ALL}\n")
    
    consent = input("Do you understand and agree? (Y/N): ").strip().upper()
    if consent != "Y":
        print("Login cancelled.")
        return

    pat = api.perform_login()
    if pat:
        store_pat(pat)
        print(Fore.GREEN + "\n✅ Success! Device authorized. You can now use `lum contribute`.")
    else:
        print(Fore.RED + "\n❌ Error: Authorization failed or timed out.")

def lum_logout(args):
    if not get_pat():
        print(Fore.YELLOW + "You are not logged in.")
        return
        
    remove_pat()
    print(Fore.GREEN + "You have been successfully logged out.")
    print("Thank you for your contributions to the Lumen network!")

def lum_contribute(args):
    import lum.api as api

    pat = get_pat()
    if not pat:
        print(Fore.RED + "You are not logged in. Please run `lum login` first.")
        return

    print("Starting contribution process...")
    root_path = os.getcwd()

    if gitignore_exists(""):
        skipped_files, skipped_folders = gitignore_skipping()
    else:
        skipped_files = get_files_parameters()["non_allowed_read"]
        skipped_folders = get_skipped_folders()
    
    allowed_files = get_files_parameters()["allowed_files"]
    
    print(" 1. Assembling file structure...")
    files_root = get_files_root(root_path, skipped_folders)
    if not files_root:
        print(Fore.YELLOW + "No allowed files found in this directory. Nothing to contribute.")
        return
    
    print(" 2. Sanitizing code and preparing payload...")
    codebase = assemble_for_api(files_root, allowed_files, skipped_files)
    
    try:
        import tiktoken
        encoding = tiktoken.get_encoding("cl100k_base")
        token_count = len(encoding.encode(codebase))
        print(f" 3. Estimated payload token count: {Fore.CYAN}{token_count}")
    except Exception:
        print(f"{Fore.YELLOW}Could not calculate token count for payload.")

    print(" 4. Submitting to Lumen network...")
    response = api.submit_contribution(pat, codebase)
    
    if response:
        print(Fore.GREEN + f"\n✅ Contribution successful! (ID: {response.get('contribution_id')})")
        print("Your submission is now in the processing queue.")
        print("You can check its status at any time with `lum history`.")
    else:
        print(Fore.RED + "\n❌ Contribution failed. Please check the error message above.")

def lum_history(args):
    import lum.api as api

    pat = get_pat()
    if not pat:
        print(Fore.RED + "You are not logged in. Please run `lum login` first.")
        return

    print("Fetching your last 10 contributions...")
    history = api.get_history(pat)

    if history is None:
        print(Fore.RED + "Could not fetch contribution history.")
        return
    
    if not history:
        print(Fore.YELLOW + "No contributions found.")
        return

    print("\n" + Style.BRIGHT + "{:<5} {:<22} {:<30} {:<15}".format("ID", "Date", "Status", "Reward ($LUM)") + Style.RESET_ALL)
    print("-" * 75)
    for item in history:
        date = item.get('created_at').split('T')[0]
        status = item.get('status', 'UNKNOWN')
        reward = item.get('reward_amount', 0.0)
        
        status_colors = {
            'PROCESSED': Fore.GREEN, 'PENDING': Fore.YELLOW, 'PROCESSING': Fore.CYAN,
        }
        status_color = status_colors.get(status, Fore.RED)

        reward_str = f"{reward:.4f}" if reward > 0 else "..."
        print("{:<5} {:<22} {}{:<30}{} {:<15}".format(
            item.get('id'), date, status_color, status, Style.RESET_ALL, reward_str
        ))
    print("-" * 75)

def print_custom_help():
    print(Fore.CYAN + Style.BRIGHT + "Lumen CLI" + Style.RESET_ALL + " - Your gateway to the Lumen Protocol and local AI context generation.")
    print(Style.DIM + "Usage: lum <command> [options]\n")

    print(Style.BRIGHT + "Network Commands" + Style.RESET_ALL + " (sends data to Lumen)")
    print(f"  {Fore.GREEN}{'login':<15}{Style.RESET_ALL} Authorize this device to contribute.")
    print(f"  {Fore.GREEN}{'contribute':<15}{Style.RESET_ALL} Sanitize and submit the current project to the network.")
    print(f"  {Fore.GREEN}{'history':<15}{Style.RESET_ALL} View the status of your recent contributions.")
    print(f"  {Fore.GREEN}{'logout':<15}{Style.RESET_ALL} De-authorize this device.")

    print("\n" + Style.BRIGHT + "Local Prompt Generation" + Style.RESET_ALL + " (does NOT send data)")
    print(f"  {Fore.CYAN}{'local [path]':<15}{Style.RESET_ALL} Analyze a directory and copy a prompt to the clipboard.")
    print(Style.DIM + "  Options for 'local':")
    print(f"    {Fore.CYAN}{'-g <URL>':<13}{Style.RESET_ALL} Analyze a public GitHub repository instead of a local path.")
    print(f"    {Fore.CYAN}{'-t <name>':<13}{Style.RESET_ALL} Save prompt to a text file (e.g., 'name.txt').")
    print(f"    {Fore.CYAN}{'-l [num]':<13}{Style.RESET_ALL} Show a leaderboard of the most token-heavy files (default: 20).")

    print("\n" + Style.BRIGHT + "Configuration" + Style.RESET_ALL)
    print(f"  {Fore.YELLOW}{'config --edit':<15}{Style.RESET_ALL} Open the configuration file for editing.")
    print(f"  {Fore.YELLOW}{'config --reset':<15}{Style.RESET_ALL} Reset all settings to their default values.")

    print("\n" + Style.DIM + "Use 'lum <command> --help' for more details on any command.")

def main():
    parser = argparse.ArgumentParser(
        description="Lumen CLI: Contribute code to the Lumen network or generate local prompts.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    parser_version = subparsers.add_parser('version', help='Show version.')

    parser_login = subparsers.add_parser('login', help='Log in and authorize this device to contribute.')
    
    parser_logout = subparsers.add_parser('logout', help='Log out and remove local credentials.')

    parser_contribute = subparsers.add_parser('contribute', help='Sanitize and contribute the current project to the Lumen network.')

    parser_history = subparsers.add_parser('history', help='View your last 10 contributions.')

    parser_local = subparsers.add_parser('local', help='Generate a local prompt without sending data.')
    parser_local.add_argument("path", nargs="?", default=os.getcwd(), help="Path to process (default: current directory).")
    parser_local.add_argument("-l", "--leaderboard", nargs="?", const=20, default=None, type=int, metavar="NUM", help="Show token leaderboard (default: 20).")
    parser_local.add_argument("-t", "--txt", metavar="FILENAME", help="Save output to a .txt file.")
    parser_local.add_argument("-g", "--github", metavar="REPO", help="Analyze a public GitHub repository.")
    
    parser_config = subparsers.add_parser('config', help='Manage configuration.')
    config_group = parser_config.add_mutually_exclusive_group(required=True)
    config_group.add_argument('--edit', action='store_true', help='Open config file for editing.')
    config_group.add_argument('--reset', action='store_true', help='Reset config to defaults.')

    args = parser.parse_args()
    check_config()

    if args.command == 'version':
        print("pylumen, version v2.0.0")

    elif args.command == 'login':
        lum_login(args)

    elif args.command == 'logout':
        lum_logout(args)

    elif args.command == 'contribute':
        lum_contribute(args)

    elif args.command == 'history':
        lum_history(args)

    elif args.command == 'config':
        if args.edit:
            print("Config file opened. Check your code editor.")
            change_parameters()
        elif args.reset:
            reset_config()

    elif args.command == 'local':
        if args.github:
            lum_github(args)
        else:
            lum_command_local(args)

    else:
        print_custom_help()

if __name__ == "__main__":
    main()