'''

Author: Callum Taylor
Filename: cw2.py

'''
## Import external libraries

import pandas as pd
import matplotlib as mpl
from tkinter import ttk
import sys

## Import external classes

import gui as gui
import analyzer as an


# Startup method to check package versions and validity
def startup():
    print("F21SC Document Tracker")
    print("Checking Pandas Version: " + pd.__version__)
    print("Checking Matplotlib Version: " + mpl.__version__)
    print("Checking Tkinter Version: " + ttk.__version__)

#gui.GUI()
an.Analyzer()

