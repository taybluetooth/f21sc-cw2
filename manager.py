'''

Author: Callum Taylor
Document: manager.py

'''
# Import external packages
import sys
import analyzer as ana
import graph as graph
import fileHandler as fh
import gui as gui

# Add termcolor text colorisation module to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
from termcolor import colored, cprint

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')

# Declare class
class Manager:

    def countries(self):
        
        """
        Controller method which calls the countries method in the analysis class.
        After successfully executing this it then executes the drawHistogram function in the graph class using the results.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        self.analyzer.countries(self.doc, self.fileHandler)
        self.graph.drawHistogram(self.analyzer.numCountries, title="Number of Countries", label="Visits by Country")
        
    def continents(self):
        
        """
        Controller method which calls the continents method in the analysis class after calculating the
        amount of countries that visitors have read the document from by using the already declared countries method.
        After successfully executing this it then executes the drawHistogram function in the graph class using the results.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        self.analyzer.countries(self.doc, self.fileHandler)
        self.analyzer.continents()
        self.graph.drawHistogram(self.analyzer.numContinents, title="Number of Continents", label="Visits by Continent")
        
    def detailedBrowser(self):
        
        """
        Controller method which calls the detailedBrowser method in the analysis class.
        After successfully executing this it then executes the drawHistogram function in the graph class using the results.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        self.analyzer.detailedBrowser(self.doc, self.fileHandler)
        self.graph.drawHistogram(self.analyzer.detailedBrowserViews, title="Visits by Browser (Detailed)", label="Number of Unique Users")

    def conciseBrowser(self):
        
        """
        Controller method which calls the conciseBrowser method in the analysis class after calculating the
        amount of browsers that visitors have used to read the document from by using the already declared detailedBrowsers method.
        After successfully executing this it then executes the drawHistogram function in the graph class using the results.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        self.analyzer.detailedBrowser(self.doc, self.fileHandler)
        self.analyzer.conciseBrowser()
        self.graph.drawHistogram(self.analyzer.conciseBrowserViews, title="Visits by Browser (Concise)", label="Number of Unique Users")

    def readerProfile(self):
        
        """
        Controller method which calls the readerProfile method in the analysis class. It then calls the sortDict method in the analysis class
        using the readers object to sort the dictionary, assigning it to the maxValues variable. This variable is then used to plot a histogram
        using the drawHistogram method found in the graph class.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        self.analyzer.readerProfile(self.fileHandler)
        maxValues = self.analyzer.sortDict(self.analyzer.readers)
        maxValues = dict(maxValues[:10])
        if maxValues:
            i = 0
            print(f"\tUser UUID\t\tTime Spent Reading (s)\n")
            for user,time in maxValues.items():
                i+=1
                print(f"{i}.\t{user}\t{time}")
            self.graph.drawHistogram(maxValues, title="Top 10 Most Avid Readers", label="Total Time Spent Reading (secs)")
        
    def alsoLikes(self):
        
        """
        Controller method which calls the alsoLikes method in the analysis class.
        It then prints a formatted table containing the method's output.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        documents = self.analyzer.alsoLikes(self.doc, self.fileHandler, self.user)
        
        if documents:
            i = 0
            print(f"\tDocument UUID\t\t\t\t\tEdges\n")
            for document in documents:
                i+=1
                print(f"{i}.\t{document[0]}\t{document[1]}")
            print("\n")
            
    def alsoLikesGraph(self):
        
        """
        Controller method which calls the alsoLikesGraph method in the analysis class.
        It then calls the directedGraph method in the graph class using the results from the previous 
        method if it exists.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        graph = self.analyzer.alsoLikesGraph(self.doc, self.fileHandler, self.user)
        if graph:
            self.graph.directedGraph(graph, self.doc, self.fileHandler.lines, self.user)

    def guiTest(self):
        
        """
        Controller method which creates a GUI instance to test task 7.

        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        gui.GUI()
        

    # Declare jobs object.
    # Job ID corresponds to methods above.
    # When job is called the associated method will execute.
    
    jobs = {
        '2A': countries,
        '2B': continents,
        '3A': detailedBrowser,
        '3B': conciseBrowser,
        '4' : readerProfile,
        '5D': alsoLikes,
        '6' : alsoLikesGraph,
        '7' : guiTest 
    }

    def assignJob(self):
        
        """
        Helper method which assigns a job and executes it if it exists in the jobs object.
        
        :param: Self references the current instance of the manager class.
        :return: Void
        """
        
        if self.doc is not None:
            print("\nExecuting task %s.\n" % str(self.job))
            self.jobs[self.job](self)
        else:
            print_red("Please specify a valid document to use.")
            
    def __init__(self, file, job, doc_uuid=None, user_uuid = None):
        
        """
        Class constructor method which initialises an instance of the manager class.
        File, job, document and user uuid's are initialised and used to
        declare the analyser, graph and fileHandler classes also.

        Method checks the job parameter's value against the jobs object declared above.
        If the job exists in the object then the job is executed.
        Otherwise an error is given.

        :param: Self references the current instance of the manager class.
        :param: File references the user inputted file that exists in the current working directory.
        :param: Job references a task ID that is called in the GUI class using the doJob method.
        :param: Doc_uuid references the user specified document uuid.
        :param: User_uuid references the user specified user uuid,
        which is default set to None as its not mandatory for analysis.
        :return: Void
        """
        
        self.file = file
        # Uppercase job input to prevent user input error
        self.job = job.upper()
        self.doc = doc_uuid
        self.user = user_uuid

        self.analyzer = ana.Analyzer()
        self.graph = graph.Graph()
        self.fileHandler = fh.FileHandler(self.file)

        if self.job not in self.jobs:
            if self.job == '2':
                while True:
                    try:
                        self.job = str(input("That is not a valid task ID. Please try 2A or 2B: ")).upper()
                        if self.job == '2A' or self.job == '2B':
                            self.assignJob()
                            break
                        print_red("Invalid task ID entered.")
                    except Exception as e:
                        print_red(e)

            elif self.job == '3':
                while True:
                    try:
                        self.job = str(input("That is not a valid task ID. Please try 3A or 3B: ")).upper()
                        if self.job == '3A' or self.job == '3B':
                            self.assignJob()
                            break
                        print_red("Invalid task ID entered.")
                    except Exception as e:
                        print_red(e)

            elif self.job == '5':
                self.job = '5D'
                print("5 is not a valid task ID. Will execute task 5D instead.")
                self.assignJob()
                
            else:
                print_red("Invalid task ID. Please try again.")
            return
        
        else:
            self.assignJob()
