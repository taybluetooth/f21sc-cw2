'''
Author: Callum Taylor
Document: fileHandler.py

'''
# Import external packages
import sys
import json
import io

# Declare class FileHandler
class FileHandler:

    # Class constructor method
    def __init__(self, file):
        self.file = file
        self.lines = 0

    # Process file method
    # Opens file and reads file line by line, yielding its json entry
    # Function only finishes when reaching an empty line
    def processFile(self):

        # Try open the file
        try:
            with io.open(self.filename, 'r', -1, 'utf-8') as f:
                for line in f:
                    self.lines += 1
                    # Use yield to allow function to continue
                    yield json.loads(line)
                    
        # Catch file not found error
        # Exit program if file does not exist
        except FileNotFoundError:
            print('The file \'%s\' does not exist in the working directory.' % str(self.file))
            sys.exit()
