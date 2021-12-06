'''

Author: Callum Taylor
Filename: cw2.py

'''
# Import external libraries

import sys


# Add modules to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
sys.path.append('lib/pycountry')
sys.path.append('lib/graphviz')

# Import lib externals
from termcolor import colored, cprint
import pycountry_convert as pycc
import graphviz as gv

import platform
import matplotlib as mpl
from tkinter import ttk
import argparse as ag

# Import external classes

import gui as gui
import manager as manager
import argsParser as args

# Initialise ArgsParser class
parser = args.ArgsParser()
# Assign arguments to global variable
arguments = parser.parse()

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')
print_blue = lambda x: cprint(x, 'white', 'on_blue')

def startup():
    
    """
    Start up method which checks versions of libraries before executing.

    :param: None
    :return: Void
    """
    
    print("\nF20SC Document Tracker")
    print("Developed by Callum Taylor\n")
    
    print("Currently running on {platform.system()} version {platform.release()}")
    print("Libraries Used:\n")
    print_blue("Argparse Version: " + ag.__version__)
    print_blue("Matplotlib Version: " + mpl.__version__)
    print_blue("Tkinter Version: " + ttk.__version__)
    
# Check arguments contains at bare minimum the execution file's name.
# If so open the GUI.

if len(sys.argv) == 1:
    startup()
    gui.GUI()
else:
    # If arguments are empty then do exit application.
    if arguments.file_name is None or arguments.doc_uuid is None or arguments.task_id is None:
        print_red('Arguments are missing or invalid. For help attach the -h argument.')
        print_blue('To open the Graphical User Interface do not attach any additional arguments.')
        sys.exit()
    else:
        startup()
        manager.Manager(arguments.file_name, arguments.task_id, arguments.doc_uuid, arguments.user_uuid)
