'''

Author: Callum Taylor
Filename: gui.py

'''

# Import external libraries

import sys
from tkinter import *
from tkinter import ttk

import manager as mn

# Add termcolor text colorisation module to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
from termcolor import colored, cprint

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')

# Declare class GUI
class GUI:

    # Action methods that are called upon clicking a button

    def countries(self):
        
        """
        Method which calls the doJob method for the counting countries functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('2A')
        
    def continents(self):
        
        """
        Method which calls the doJob method for the counting continents functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('2B')

    def detailedBrowser(self):
        
        """
        Method which calls the doJob method for the detailed browser (OS & Version included) visits functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('3A')

    def conciseBrowser(self):
        
        """
        Method which calls the doJob method for the concise browser (Main Browser Name only) visits functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void   
        """
        
        self.doJob('3B')

    def readerProfile(self):
        
        """
        Method which calls the doJob method for the top 10 most avid readers functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('4')

    def alsoLikes(self):
        
        """
        Method which calls the doJob method for the also likes functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('5D')

    def alsoLikesGraph(self):
        
        """
        Method which calls the doJob method for the also likes graph generation functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void
        """
        
        self.doJob('6')

    def guiTest(self):
        
        """
        Method which calls the doJob method for the gui test functionality.
        
        :param: Self references the current instance of the GUI class.  
        :return: Void    
        """
        
        self.doJob('7')

    def doJob(self, job):
        
        """
        Helper method which executes a job by calling the manager constructor passing in
        a specified job, the user and document uuid's and the filename. If the job is valid in the
        manager class it will then execute the corresponding job.
        
        :param: Self references the current instance of the GUI class.
        :param: Job references a task ID as initialised in the manager class,
        (eg. 2A corresponds to requirement 2A).
        :return: Void
        """
        
        # Strip whitespace from both user and document uuid's        
        user = self.userID.get().strip()
        filename = self.filename.get()
        document = self.documentID.get().strip()

        if(job != '4'):
            if document == "" or filename == "":
                print_red("Please enter at least both a document uuid and filename")
            else:
                self.root.destroy()
                mn.Manager(filename, job, document, user)
        else:
            if filename == "":
                print_red("Please enter a filename to calculate top 10 most avid readers.")
            else:
                self.root.destroy()
                mn.Manager(filename, job, document, user)
    
    def __init__(self):
        
        """
        Class constructor function which initalises the GUI.
        Window dimensions, text input, buttons and labels are all initialised and configured here.

        :param: Self references the current instance of the GUI class.
        :return: Void
        """
        
        self.root = Tk()
        self.root.title("F20SC CW2")

        # Set window dimensions and layout
        mainframe = ttk.Frame(self.root, padding="12 12 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Action buttons
        # Text represents functionality as referenced in specification
        
        ttk.Button(mainframe, text="2A", command=self.countries).grid(column=2, row=4)
        ttk.Button(mainframe, text="2B", command=self.continents).grid(column=3, row=4)
        ttk.Button(mainframe, text="3A", command=self.detailedBrowser).grid(column=4, row=4)
        ttk.Button(mainframe, text="3B", command=self.conciseBrowser).grid(column=5, row=4)
        ttk.Button(mainframe, text="4", command=self.readerProfile).grid(column=2, row=5)
        ttk.Button(mainframe, text="5D", command=self.alsoLikes).grid(column=3, row=5)
        ttk.Button(mainframe, text="6", command=self.alsoLikesGraph).grid(column=4, row=5)
        ttk.Button(mainframe, text="7", command=self.guiTest).grid(column=5, row=5)

        # Labels for text input fields
        ttk.Label(mainframe, text="User UUID:").grid(column=1, row=1, sticky=E)
        ttk.Label(mainframe, text="Document UUID:").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Filename:").grid(column=1, row=3, sticky=E)

        # Text input fields
        self.userID = StringVar()
        self.documentID = StringVar()
        self.filename = StringVar()

        user_input = ttk.Entry(mainframe, width=7, textvariable=self.userID)
        user_input.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        doc_input = ttk.Entry(mainframe, width=7, textvariable=self.documentID)
        doc_input.grid(column=2, row=2, columnspan=2, sticky=(W, E))
        file_input = ttk.Entry(mainframe, width=7, textvariable=self.filename)
        file_input.grid(column=2, row=3, columnspan=2, sticky=(W, E))


        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        doc_input.focus()

        self.root.mainloop()
