'''

Author: Callum Taylor
Document: graph.py

'''

# Import external packages
import sys
import matplotlib.pyplot as mpl
import random

# Declare graph class
class Graph:

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
