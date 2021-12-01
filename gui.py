'''

Author: Callum Taylor
Filename: gui.py

'''

# Import external libraries

from tkinter import *
from tkinter import ttk

import manager as mn


# Declare class GUI
class GUI:

    # Action methods that are called upon clicking a button

    """

    Method which calls the doJob method for the counting countries functionality.
    
    :param: Self references the current instance of the GUI class.  
    :return: Void
    
    """
    def countries(self):
        self.doJob('2A')

    """

    Method which calls the doJob method for the counting continents functionality.
    
    :param: Self references the current instance of the GUI class.  
    :return: Void
    
    """
        
    def continents(self):
        self.doJob('2B')

    def largeBrowser(self):
        print("Full Browser")

    def shortBrowser(self):
        print("Short Browser")

    def alsoLikes(self):
        print("Also Likes")

    def alsoLikesGraph(self):
        print("Also Likes Graph")

    """

    Helper method which executes a job by calling the manager constructor passing in
    a specified job, the user and document uuid's and the filename. If the job is valid in the
    manager class it will then execute the corresponding job.
    
    :param: Self references the current instance of the GUI class.
    :param: Job references a task ID as initialised in the manager class,
    (eg. 2A corresponds to requirement 2A).
    :return: Void
    
    """

    def doJob(self, job):
        user = self.userID.get()
        filename = self.filename.get()
        document = self.documentID.get()

        if document == "" or filename == "":
            print("Please enter at least both a document uuid and filename")
        else:
            self.root.destroy()
            mn.Manager(filename, job, document, user)

    """

    Class constructor function which initalises the GUI.
    Window dimensions, text input, buttons and labels are all initialised and configured here.

    :param: Self references the current instance of the GUI class.
    :return: Void
    
    """
    
    def __init__(self):
        self.root = Tk()
        self.root.title("F21SC CW2")

        # Set window dimensions and layout
        mainframe = ttk.Frame(self.root, padding="20 20 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Text input fields
        self.userID = StringVar()
        self.documentID = StringVar()
        self.filename = StringVar()

        userID_entry = ttk.Entry(mainframe, width=7, textvariable=self.userID)
        userID_entry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        docID_entry = ttk.Entry(mainframe, width=7, textvariable=self.documentID)
        docID_entry.grid(column=2, row=2, columnspan=2, sticky=(W, E))
        filename_entry = ttk.Entry(mainframe, width=7, textvariable=self.filename)
        filename_entry.grid(column=2, row=3, columnspan=2, sticky=(W, E))

        # Action buttons
        # Text represents functionality as referenced in specification
        ttk.Button(mainframe, text="2A", command=self.countries).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text="2B", command=self.continents).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text="3A", command=self.largeBrowser).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text="3B", command=self.shortBrowser).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text="4D", command=self.alsoLikes).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text="5", command=self.alsoLikesGraph).grid(column=3, row=5, sticky=W)

        # Labels for text input fields
        ttk.Label(mainframe, text="User UUID:").grid(column=1, row=1, sticky=E)
        ttk.Label(mainframe, text="Document UUID:").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Filename:").grid(column=1, row=3, sticky=E)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        docID_entry.focus()

        self.root.mainloop()
