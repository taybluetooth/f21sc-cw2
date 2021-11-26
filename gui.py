'''

Author: Callum Taylor
Filename: gui.py

'''

# Import external libraries

from tkinter import *
from tkinter import ttk


# Declare class GUI
class GUI:

    # Action methods that are called upon clicking a button
    def countries(self):
        print("Countries")
        
    def continents(self):
        print("Continents")

    def largeBrowser(self):
        print("Full Browser")

    def shortBrowser(self):
        print("Short Browser")

    def alsoLikes(self):
        print("Also Likes")

    def alsoLikesGraph(self):
        print("Also Likes Graph")

    # Class constructor method
    def __init__(self):
        self.root = Tk()
        self.root.title("F21SC CW2")

        # Set window dimensions and layout
        mainframe = ttk.Frame(self.root, padding="14 14 14 14")
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
        ttk.Label(mainframe, text="Document UUID").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Filename").grid(column=1, row=3, sticky=E)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        docID_entry.focus()

        self.root.mainloop()
