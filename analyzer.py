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

# Declare analyzer class
class Analyzer:

    numCountries = {}
    numContinents = {}

    """
    Method which calculates the amount of visits from different countries.

    Reads each line processed by the fileHandler class for visitors' countries,
    the event enacted on the document and checking if it was read. The document uuid is also presence checked.
    
    :param: Self references the current instance of the Analyzer class.
    :param: documentID references the user inputted document uuid.
    :file: file references the user inputted file 
    :return: Void

    """

    def countries(self, documentID, file):
        for record in file.processFile():
            if 'visitor_country' in record and 'event_type' in record and 'subject_doc_id' in record:
                if record['event_type'] == 'read':
                    if str(record['subject_doc_id']) == documentID:
                        if record['visitor_country'] in self.numCountries:
                            self.numCountries[record['visitor_country']] += 1
                        else:
                            self.numCountries[record['visitor_country']] = 1

    """
    Method which calculates the amount of visits from different continents.
    
    Uses the numCountries object and the pyconvert package to convert country codes
    into their corresponding continents. These are then added to the numContinents object global.

    :param: Self
    :return: Void

    """
    def continents(self):
        if len(self.numCountries) == 0:
            print("No data has been provided. Please check document's data is correct.")
            return
        else:
            for countryCode in self.numCountries:
                try:
                    continentEntry = pycc.country_alpha2_to_continent_code(countryCode)
                except KeyError:
                    print('%s could not be allocated a continent.' % countryCode)
                    continue
                except:
                    print('%s could not be converted to a continent' % countryCode)
                    continue

                if continentEntry in self.numContinents:
                    self.continentCounts[continentEntry] += 1
                else:
                    self.continentCounts[continentEntry] = 1
        

    def largeBrowser():
        print("Large Browser")

    def shortBrowser():
        print("Short Browser")

    def alsoLikes():
        print("Also Likes")

    def alsoLikesGraph():
        print("Also Likes Graph")

    def __init__(self):
        print("Analyzer")
    
