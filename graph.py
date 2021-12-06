'''

Author: Callum Taylor
Document: graph.py

'''

# Import external packages
import sys
import matplotlib.pyplot as mpl
import random

# Add graphviz to system path variable
# Neccesary step to import
sys.path.append('lib/graphviz')
# Import directed graph module
from graphviz import Digraph

# Add termcolor text colorisation module to system path variable
# Necessary step to import
sys.path.append('lib/termcolor')
from termcolor import colored, cprint

# Create functions for printing coloured messages.
print_red = lambda x: cprint(x, 'white', 'on_red')

# Declare graph class
class Graph:

    file = "DirectedGraph"

    """
    Draws a histogram graph given data that can be represented a constant
    and plotted accordingly.

    :param: Data references the data to be plotted in the graph
    :param: Label references the label to be shown adjacent to the bar(s) in the graph.
    :param: Title references the title assigned to matplotlib.
    :return: Void
    
    """
    def drawHistogram(self, data, label="Data", title="Default"):

        # Generate random bar colour to help distinguish data
        r = lambda: random.randint(0,255)       
        bar_colors = []

        # x and y axis tick locations to variables
        bar_fun = mpl.bar
        bar_ticks = mpl.xticks
        bar_label = mpl.ylabel

        n = len(data)

        for i in range(0,n):
            bar_colors.append('#{:02x}{:02x}{:02x}'.format(r(), r(), r()))
        
        # Map data onto graph using data values and keys           
        bar_fun(range(n), list(data.values()), align='center', color=bar_colors, alpha=0.4)
        bar_ticks(range(n), list(data.keys()))
        bar_label(label)

        # Assign graph title and display         
        mpl.title(title)
        mpl.show()

    def shortenNumber(self, number):
        number = number / 2
        number = float('{:.3g}'.format(number))
        size = 0
        while abs(number) >= 1000:
            size += 1
            number /= 1000.0
        return '{}{}'.format('{:f}'.format(number).rstrip('0').rstrip('.'), ['', 'K', 'M'][size])

    """
    https://graphviz.readthedocs.io/en/stable/manual.html
    """
    def directedGraph(self, data, documentID, lines, visitorID=None):
        
        if type(data) != dict:
            print_red('Invalid data type given. Please use a valid data type suitable for digraph plotting.'% str(type(data)))
            return

        # Change line formatting to match test data expectations
        # Use floor division to determine if line count is in 1,000's or 1,000,000's

        lines = self.shortenNumber(lines)
        size = str(lines)

        graph = Digraph(name='Directed Graph')
        graph.node('Documents', shape='none')
        graph.node('Visitors', shape='none')
        graph.edge('Visitors', 'Documents', label=('Size: %s' % size))

        try:
            for visitor in data:
                if visitor == visitorID:
                    graph.node(str(visitor)[-4:], fillcolor='green', shape='box', style='filled')
                else:
                    graph.node(str(visitor)[-4:], shape='box')
                for document in data[visitor]:
                    if document == documentID:
                        graph.node(str(document)[-4:], fillcolor='green', style='filled')
                    else:
                        graph.node(str(document)[-4:])
                    graph.edge(str(visitor)[-4:], str(document)[-4:])
        except TypeError:
            print_red('Invalid type: Type is not suitable for directedGraph method.')
        except:
            print_red('Error when creating directed graph.')

        try:
            graph.render(self.file, view=True)
        except:
            print_red('Cannot save graph to file with filename %s' % self.file)
        
