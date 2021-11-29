'''
Author: Callum Taylor
Document: manager.py

'''

# Declare class
class Manager:

    def countries(self):
        print("Count Countries")
        
    def continents(self):
        print("Count Continents")

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
        '2B': countContinents,
        '3A': countFullBrowser,
        '3B': countShortBrowser,
        '4D': alsoLikes,
        '5': alsoLikesGraph
    }

    # Declare class constructor method   
    def __init__(self, file, job, doc_uuid, user_uuid = None):
        self.filename = filename
        self.job = job_id
        self.doc = doc_uuid
        self.user = user_uuid

        if self.job not in self.jobs:
            print(' '% self.job)
        else:
            if self.inputDoc is not None:
                self.jobs[self.job](self)
            else:
                print('Please specify a document to use.')
