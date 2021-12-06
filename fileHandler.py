'''

Author: Callum Taylor
Document: fileHandler.py

'''
# Import external packages
import sys
import json
import io

# Add termcolor text colorisation module to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
from termcolor import colored, cprint

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')

# Declare class FileHandler
class FileHandler:

    """
    Class constructor method which initialises an instance of the fileHandler
    class. The file to be read is initialised by a parameter and a lines constant
    is declared.

    :param: Self references the current instance of the fileHandler class.
    :param: File references the file to be processed and read.
    :return: Void
    """
    def __init__(self, file):
        self.file = file
        self.lines = 0

    # Process file method
    # Opens file and reads file line by line, yielding its json entry
    # Function only finishes when reaching an empty line
    """
    Method which processes the file declared in the constructor. File is opened
    and read line by line, yielding an entry which is processed by the json package.
    If file is not found it is handled by the FileNotFoundError exception handler.

    :param: Self references the current instance of the fileHandler class.
    :return: Void
    """
    def processFile(self):

        # Try open the file
        try:
            with io.open(self.file, 'r', -1, 'utf-8') as f:
                for line in f:
                    self.lines += 1
                    # Use yield to allow function to continue
                    yield json.loads(line)
                    
        # Catch file not found error
        # Exit program if file does not exist
        except FileNotFoundError:
            print_red('The file \'%s\' does not exist in the working directory.' % str(self.file))
            sys.exit()
