'''

Author: Callum Taylor
Document: analyzer.py

'''

# Import external packages
import sys
import operator

# Add pycountry convert package to system path variable
# Necessary step to import
sys.path.append('lib/pycountry')
import pycountry_convert as pycc

# Add termcolor text colorisation module to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
from termcolor import colored, cprint

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')

# Declare analyzer class
class Analyzer:

    # Declare global data dictionaries
    numCountries = {}
    numContinents = {}
    detailedBrowserViews = {}
    conciseBrowserViews = {}
    readers = {}

    def countries(self, documentID, file):
        
        """
        Method which calculates the amount of visits from different countries.

        Reads each line processed by the fileHandler class for visitors' countries,
        the event enacted on the document and checking if it was read. The document uuid is also presence checked.
        
        :param: Self references the current instance of the Analyzer class.
        :param: documentID references the user inputted document uuid.
        :file: file references the file being read by the fileHandler class.
        :return: Void
        """
        
        for record in file.processFile():
            if 'visitor_country' in record and 'event_type' in record and 'subject_doc_id' in record:
                if record['event_type'] == 'read' or record['event_type'] == 'pageread' or record['event_type'] == 'pagereadtime':
                    if str(record['subject_doc_id']) == documentID:
                        if record['visitor_country'] in self.numCountries:
                            self.numCountries[record['visitor_country']] += 1
                        else:
                            self.numCountries[record['visitor_country']] = 1

    def continents(self):
        
        """
        Method which calculates the amount of visits from different continents.
        
        Uses the numCountries object and the pyconvert package to convert country codes
        into their corresponding continents. These are then added to the numContinents object global.

        :param: Self references the current instance of the Analyzer class.
        :return: Void
        """
        
        if len(self.numCountries) == 0:
            print_red("No data has been provided. Please check the document's data is correct.")
            return
        else:
            for countryCode in self.numCountries:
                try:
                    continentEntry = pycc.convert_country_alpha2_to_continent(countryCode)
                except KeyError:
                    print_red('KeyError: %s could not be found as a valid country code.' % countryCode)
                    continue


                if continentEntry in self.numContinents:
                    self.numContinents[continentEntry] += 1
                else:
                    self.numContinents[continentEntry] = 1
        
    def detailedBrowser(self, documentID, file):
        
        """
        Method which calculates how many unique browsers have been used to visit a document.
        Data produced is very in depth describing browser versioning and the operating system used.

        Reads each line processed by the fileHandler class and checks if a document has been read.
        If the visitors browser is already present in the browser views object which counts visitations, then it will add another to this count.
        Otherwise it will create an attribute in the object with an initial value of 1 representing this browser.

        :param: Self references the current instance of the Analyzer class.
        :param: documentID references the user inputted document uuid.
        :param: file references the file being read by the fileHandler class.
        :return: Void  
        """
        
        for record in file.processFile():
            if 'event_type' in record and 'visitor_useragent' in record:
                if record['event_type'] == 'read' or record['event_type'] == 'pageread' or record['event_type'] == 'pagereadtime':
                    if str(record['subject_doc_id']) == documentID:
                        if record['visitor_useragent'] in self.detailedBrowserViews:
                            self.detailedBrowserViews[record['visitor_useragent']] += 1
                        else:
                            self.detailedBrowserViews[record['visitor_useragent']] = 1
                            
    def conciseBrowser(self):
        
        """
        Method which calculates how many unique browsers have been used to visit a document.
        Data produced is more concise showing only the browser's name.

        Uses the data gathered by the detailedBrowser method and then performs string manipulation to shorten
        and parse the data to extract the browsers name. If this name is present already in the conciseBrowserViews object,
        it's count is increased by 1, otherwise it will create an attribute in the object with an initial value of 1 representing this browser.
        
        :param: Self references the current instance of the Analyzer class.
        :return: Void     
        """     
                 
        if len(self.detailedBrowserViews) == 0:
            print_red("No data has been provided. Please check the document's data is correct.")
            return
        else:
            for browser in self.detailedBrowserViews:
                name = browser.split('/')[0] + ' ' + browser.split('/')[-2].split(' ')[-1]
                if name in self.conciseBrowserViews:
                    self.conciseBrowserViews[name] += self.detailedBrowserViews[browser]
                else:
                    self.conciseBrowserViews[name] = self.detailedBrowserViews[browser]

    def readerProfile(self, file):    
        
        """
        Method which calculates the total amount of time users have spent reading all documents in a dataset.

        Reads each line checking for event types consisting of either read, pageread or pagereadtime. The first 2 do not have time
        specific values, so according to issuu data documentation, 2 seconds is assumed. However pagereadtime has a time specific value,
        stating that it is calculated after 2 seconds has passed in milliseconds, this value is converted into seconds and added on to 2 seconds.
        These values are then stored in the readers object.
        
        :param: Self references the current instance of the Analyzer class.
        :param: file references the file being read by the fileHandler class.
        :return: Void
        """
        
        for record in file.processFile():
            if 'visitor_uuid' in record and 'subject_doc_id' in record and 'event_type' in record:
                if record['event_type'] == 'read' or record['event_type'] == 'pageread':
                    if record['visitor_uuid'] in self.readers:
                        self.readers[record['visitor_uuid']] += 2
                    else:
                        self.readers[record['visitor_uuid']] = 2
                elif record['event_type'] == 'pagereadtime':
                    if record['visitor_uuid'] in self.readers:
                        self.readers[record['visitor_uuid']] += (record['event_readtime'] / 1000) + 2
                    else:
                        self.readers[record['visitor_uuid']] = (record['event_readtime'] / 1000) + 2
    
    def sortDict(self, dictionary):
        
        """
        Method which sorts a dictionary into descending order based on value and returns sorted result.
        
        :param: Self references the current instance of the Analyzer class.
        :param: dictionary references the input dictionary to be sorted by the method.
        :return: Output dictionary sorted in descending order. 
        """
        
        output = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
        return output

    def docVisitors(self, documentID, file):
        
        """
        Method which returns all visitor uuid's of a document given a specified document.

        Reads each line processed by the fileHandler class for visitors who have a matching subject_doc_id with
        the specified document. If there is a match the document is added to a list of documents read by the visitor.
        This list is then returned.
        
        :param: Self references the current instance of the Analyzer class.
        :param: documentID references the user inputted document uuid.
        :param: file references the file being read by the fileHandler class.
        :return: Void
        """
        
        documents = []
        
        for record in file.processFile():
            if 'visitor_uuid' in record and 'subject_doc_id' in record and 'event_type' in record:
                if record['event_type'] == 'read' or record['event_type'] == 'pageread' or record['event_type'] == 'pagereadtime':
                    if str(record['subject_doc_id']) == documentID:
                        documents.append(record['visitor_uuid'])
        return documents

    def parseDocVisitors(self, file):
        
        """
        Method which returns all visitor uuid's of a document given a specified document.

        Reads each line processed by the fileHandler class for visitors who have a matching subject_doc_id with
        the specified document. If there is a match the visitor is added to a list of visitors who read the document.
        This list is then returned.
        
        :param: Self references the current instance of the Analyzer class.
        :param: file references the file being read by the fileHandler class.
        :return: visitors object containing all a document's visitors
        """
        
        visitors = {}

        for record in file.processFile():
            if 'visitor_uuid' in record and 'subject_doc_id' in record and 'event_type' in record:
                if record['event_type'] == 'read':

                    document = record['subject_doc_id']
                    visitor = record['visitor_uuid']

                    if document in visitors:
                        if visitor not in visitors[document]:
                            visitors[document].append(visitor)
                    else:
                        visitors[document] = [visitor]

        return visitors

    def parseUserDocuments(self, file):
        
        """
        Method which returns all document uuid's a visitor has read given a specified visitor.

        Reads each line processed by the fileHandler class for documents who have been read by a specified visitor. 
        If there is a match the document is added to a list of documents read by the visitor.
        This list is then returned.
        
        :param: Self references the current instance of the Analyzer class.
        :param: file references the file being read by the fileHandler class.
        :return: documents object that contains all a user's read documents
        """
        
        documents = {}

        for record in file.processFile():
            if 'visitor_uuid' in record and 'subject_doc_id' in record and 'event_type' in record:
                if record['event_type'] == 'read':

                    document = record['subject_doc_id']
                    visitor = record['visitor_uuid']

                    if visitor in documents:
                        if document not in documents[visitor]:
                            documents[visitor].append(document)
                    else:
                        documents[visitor] = [document]
        return documents            

    def alsoLikes(self, documentID, file, visitorID=None):
        
        """
        Method which generates the also likes function as specified in the requirements. 
        Generates a sorted list of documents a visitor might like based on a given document ID.
        Uses the parseDocVisitors and parseUserDocument methods to gather a document's visitors and a visitor's documents read.      
        
        :param: Self references the current instance of the Analyzer class.
        :param: documentID references a document's uuid.
        :param: file references the file being read by the fileHandler class.
        :param: visitorID references a visitor's uuid.
        :return: sortedResult that contains sorted alsoLikes result in desc order limited to 10 entries.
        """

        docVisitors = self.parseDocVisitors(file)
        documents = self.parseUserDocuments(file)

        output = {}

        if documentID in docVisitors:
            for visitor in docVisitors[documentID]:
                if visitor != visitorID:
                    for document in documents[visitor]:
                        if document != documentID:
                            if document in output:
                                output[document] += 1
                            else:
                                output[document] = 1
        else:
            print_red("%s was not present in the dataset. Please try another document." % str(documentID))
            return

        sortedResult = self.sortDict(output)
        if len(sortedResult) > 10:
            sortedResult = sortedResult[:10]
        return sortedResult

    def alsoLikesGraph(self, documentID, file, visitorID=None):
        
        """
        Method which generates the also like graph's data object to use in the graph class.
        Returns an object containing the necessary data to plot the directed graph.
        
        :param: Self references the current instance of the Analyzer class.
        :param: documentID references the user inputted document uuid.
        :file: file references the file being read by the fileHandler class.
        :return: output object containing document and edge pairs.
        """
        
        docVisitors = self.parseDocVisitors(file)
        documents = self.parseUserDocuments(file)
        output = {}

        if documentID in docVisitors:
            visitors = docVisitors[documentID]
        else:
            print_red("Document %s not found in data set" % str(documentID))
            return

        for user in documents:
            if user == visitorID:
                output[user] = [documentID]
            else:
                if user in visitors and not documents[user] == [documentID]:
                    output[user] = documents[user]
        return output
    
