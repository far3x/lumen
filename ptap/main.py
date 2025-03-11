from ptap.visualizer import *
from ptap.assembly import *
from ptap.config import *

from typing import List
import json, argparse, os

"""
Idea : 

You're in the terminal, you type "ptap" only, it shows the full structure of the actual directory you're in with the settings you have, or base settings if you didn't change anything
So a structured prompt with the path structure in a json format, then each file title and file content, spaced correctly

Options :
 FUNC DONE - give the path manually if you're not directly in the correct directory
 NOT  DONE - change skipped folders (stocked in pc memory) (so not ignore some folders content like ".git" or whatever folder that we don't want to give to a prompt)
 NOT  DONE - specify the output (base case = will be in clipboard), but would be able to generate a .txt in the selected folder to be able to change some content in the file manually
 NOT  DONE - change intro/title content "ptap -c intro" would show the intro, and give possibility to change it, same with title, with {}'s or f string or wtv
 FUNC DONE - reset settings "ptap -r" would reset everything
 FUNC DONE - not include or hide file intro, structure, or whatever "ptap -h intro" or "ptap -h intro,structure,title"

After each pip update, keep the settings so the user would not lose any content that was changed like title, intro etc
"""



#when the user types ptap, initializes check_config() then we add all options like in the file base


base_parameters = {
    "intro_text": get_intro(),
    "show_intro": get_intro_status(),
    "title_text": get_title(),
    "show_title": get_title_status(),
    "skipped_folders": get_skipped_folders()
}

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

def change_parameter(parameter: str = None):
    if parameter is not None:
        pass
        #go to json and change the parameter


def make_structure(path: str = None, skipped: List = base_parameters["skipped_folders"]):
    #when user types a path, we use this function with an argument, otherwise no argument and get automatically the path
    if path: root_path = path
    else: root_path = os.getcwd()

    data = json.dumps( 
        get_project_structure(
            root_path = root_path, 
            skipped_folders = skipped
        ),
        indent = 4,
    )

    return data

