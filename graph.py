'''

Author: Callum Taylor
Document: graph.py

'''

# Import external packages
import sys
import matplotlib.pyplot as mpl

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
        
        bar_fun = mpl.barh
        bar_ticks = mpl.yticks
        bar_label = mpl.xlabel

        n = len(data)
        bar_fun(range(n), list(data.values()), align='center', alpha=0.4)
        bar_ticks(range(n), list(data.keys()))
        bar_label(label)
        mpl.title(title)
        mpl.show()
