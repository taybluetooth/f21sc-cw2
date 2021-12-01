'''

Author: Callum Taylor
Filename: cw2.py

'''
# Import external libraries

import sys
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

"""
Start up method which checks versions of libraries before executing.

:param: None
:return: Void

"""
def startup():
    print("F20SC Document Tracker")
    print("Checking Argparse Version: " + ag.__version__)
    print("Checking Matplotlib Version: " + mpl.__version__)
    print("Checking Tkinter Version: " + ttk.__version__)
    
# Check arguments contains at bare minimum the execution file's name.
# If so open the GUI.
if len(sys.argv) == 1:
    gui.GUI()
else:
    # If arguments are empty then do exit application.
    if arguments.file_name is None or arguments.doc_uuid is None or arguments.task_id is None:
        print('Arguments are missing or invalid. For help attach the -h argument.')
        print('To open the Graphical User Interface do not attach any additional arguments.')
        sys.exit()
    else:
        manager.Manager(arguments.file_name, arguments.task_id, arguments.docu_uuid, args.user_uuid)
