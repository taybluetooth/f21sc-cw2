'''

Author: Callum Taylor
Filename: DocumentTracker.py

'''
## Import external libraries

import pandas as pd
import matplotlib as mpl
from tkinter import ttk

'''

Start up method to initialise application
and perform checks on libraries.

Parameters: None
Returns: None

'''

def startup():
    print("F21SC Document Tracker")
    print("Running Pandas Version: " + pd.__version__)
    print("Running Matplotlib Version: " + mpl.__version__)
    print("Running Tkinter Version: " + ttk.__version__)

startup()
    


