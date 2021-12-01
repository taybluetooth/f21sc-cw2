'''
Author: Callum Taylor
Document: manager.py

'''

import analyzer as ana
import graph as graph
import fileHandler as fh

# Declare class
class Manager:

    """
    Controller method which calls the countries method in the analysis class.
    After successfully executing this it then executes the drawHistogram function in the graph class.

    :param: Self references the current instance of the manager class.
    :return: Void
    """
    def countries(self):
        self.analyzer.countries(self.doc, self.fileHandler)
        self.graph.drawHistogram(self.analyzer.numCountries, title="Number of Countries", label="Visits by Country")
        
    """
    Controller method which calls the continents method in the analysis class after calculating the
    amount of countries that visitors have read the document from by using the already declared countries method.
    After successfully executing this it then executes the drawHistogram function in the graph class.

    :param: Self references the current instance of the manager class.
    :return: Void
    """
    
    def continents(self):
        self.analyzer.countries(self.doc, self.fileHandler)
        self.analyzer.continents()
        self.graph.drawHistogram(self.analyzer.numContinents, title="Number of Continents", label="Visits by Continent")
        

    def largeBrowser(self):
        print("Large Browser")

    def shortBrowser(self):
        print("Short Browser")

    def alsoLikes(self):
        print("Also Likes")

    def alsoLikesGraph(self):
        print("Also Likes Graph")

    # Declare jobs object
    jobs = {
        '2A': countries,
        '2B': continents,
        '3A': largeBrowser,
        '3B': shortBrowser,
        '4D': alsoLikes,
        '5': alsoLikesGraph
    }

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
    def __init__(self, file, job, doc_uuid, user_uuid = None):
        
        self.file = file
        self.job = job
        self.doc = doc_uuid
        self.user = user_uuid

        self.analyzer = ana.Analyzer()
        self.graph = graph.Graph()
        self.fileHandler = fh.FileHandler(self.file)

        if self.job not in self.jobs:
            print(' '% self.job)
        else:
            if self.doc is not None:
                self.jobs[self.job](self)
            else:
                print('Please specify a document to use.')
