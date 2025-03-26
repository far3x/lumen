import shutil
import sys
import requests
import subprocess
import stat
import os
from ptap.config import *

#i fixed few functions with ai, the simplest way possible, just bcs of permission errors when deleting the cloned repo :/


def make_github_api_link(repo_link: str = None):
    #we need to make link a https in case the user inputs a bad link
    #case 2 : github.com/... -> https://githu...
    #case 3 : https:// = good
    #also for the git clone, need .git at the end

    if repo_link is None:
        return False, False
    if repo_link.startswith("http://"):
        print("Use a secured link please (https:// and not http://)")
        return False, False

    clone_link = repo_link if repo_link.endswith(".git") else repo_link + ".git"
    api_proc_link = repo_link[:-4] if repo_link.endswith(".git") else repo_link

    links = ["https://github.com/", "https://www.github.com/", "github.com/", "www.github.com/"]
    for link_prefix in links:
        if api_proc_link.startswith(link_prefix):
            rest = api_proc_link.split(link_prefix, 1)[-1]
            if '/' in rest and not rest.startswith('/') and not rest.endswith('/'):
                 return "https://api.github.com/repos/" + rest, clone_link

    print("Link does not appear to be a standard GitHub repository link.")
    return False, False


def check_repo(repo_link: str = None):
    api_link, _ = make_github_api_link(repo_link=repo_link)
    if api_link:
        try:
            headers = {
                'User-Agent': 'PTAP-Python-Script'
            }

            response = requests.get(url=api_link, timeout=10, headers=headers)
            return response.status_code == 200 #true if exists otherwise false !
        except requests.exceptions.RequestException as e:
            print(f"ERROR checking repository API: {e}")

    return False #false if link can't be secured or doesn't exist or isnt github link


def check_git():
    if shutil.which('git') is None:
        print("Git is not installed. Please install it manually.")

        if sys.platform.startswith('win'):
            print("On Windows: https://git-scm.com/download/win")
        elif sys.platform.startswith('linux'):
            print("On Linux: Use package manager (e.g., 'sudo apt install git' or 'sudo yum install git').")
        elif sys.platform.startswith('darwin'):
            print("On macOS: https://git-scm.com/download/mac or 'brew install git'.")

        return False
    return True


def remove_readonly(func, path, excinfo):
    exc_value = excinfo[1]
    if isinstance(exc_value, PermissionError) or \
       (hasattr(exc_value, 'winerror') and exc_value.winerror == 5):
        try:
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            func(path) #retry
        except Exception as e:
            raise exc_value from e #raise if retry/fix failed XD
    else:
        raise exc_value #other


def download_repo(repo_link: str = None):
    if not repo_link:
        raise ValueError("Repository link is required.")

    _, clone_link = make_github_api_link(repo_link=repo_link)
    if not clone_link:
        raise ValueError("Invalid or unsupported GitHub repository link format.")

    #go to ptap config file
    ptap_repo = get_config_directory()
    repo_name = clone_link.split("/")[-1].replace(".git", "")
    if not repo_name: 
        repo_name = clone_link.split("/")[-2] #trailing slash case
    ptap_repo_name = os.path.join(ptap_repo, repo_name)

    #removing existing folder if already exists
    if os.path.exists(ptap_repo_name):
        print(f"Removing existing directory: {ptap_repo_name}")
        remove_repo(ptap_repo_name)

    #download with git clone using the parameter
    command = ["git", "clone", clone_link, ptap_repo_name]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True) #check will raise an error if there is one with the git clone command, didnt know
        #return the path of the folder to analyze
        return ptap_repo_name
    except subprocess.CalledProcessError as e:
        print(f"Git clone failed. Error: {e.stderr}")
        if os.path.exists(ptap_repo_name):
            print("Attempting cleanup of partially cloned folder...")
            remove_repo(ptap_repo_name)
        raise #force exception, didnt know this exists thats so nice


def remove_repo(repo_root: str = None):
    if not repo_root or not isinstance(repo_root, str) or not os.path.isdir(repo_root):
        print(f"Path not found or not a directory: {repo_root}")
        return

    try:
        shutil.rmtree(repo_root, onerror=remove_readonly) #if permissions error we remove the readonly to be able to delete the folder we cloned
    except Exception as e:
        print(f"ERROR deleting folder {repo_root}: {e}")