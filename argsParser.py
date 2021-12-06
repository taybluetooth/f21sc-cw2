'''

Author: Callum Taylor
Filename: argsParser.py

'''

# Import external libraries
import argparse as ag

# Declare ArgsParser class
class ArgsParser:

    def parse(self): 
        
        """
        Method which returns the parsed arguments declared
        in the constructor function.
        
        :param: Self references the current instance of the ArgsParser class.
        :return: Parsed arguments
        """ 
        
        parsed = self.root.parse_args()
        return parsed

    def __init__(self):
        
        """
        Constuctor function which initialises the class and assigns attributes to it.
        Argument parser is declared as the root attribute and arguments are then added to root.

        :param: Self references the current instance of the ArgsParser class.
        :return: Void
        """
       
        # Declare arguments parser
        self.root = ag.ArgumentParser()

        # Assign valid arguments to the parser
        self.root.add_argument("-u", "--user_uuid", type = str, help = "User ID of visitor being searched")
        self.root.add_argument("-d", "--doc_uuid", type = str, help = "Document ID of the document being searched")
        self.root.add_argument("-t", "--task_id", type = str, help = "Task ID corresponding to task to be executed.")
        self.root.add_argument("-f", "--file_name", type=  str, help = "File storing the dataset to be analysed in .json format.")
