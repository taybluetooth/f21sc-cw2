'''

Author: Callum Taylor
Document: graph.py

'''

# Import external packages
import sys
sys.path.append("graphviz-0.10.1")

import matplotlib.pyplot as plt
from graphviz import Digraph

# Declare class
class Graph:

    savename = 'dot_graph'

    '''
    Method which draws a historgram from a dictionary.
    Count represents value to be shown in the graph and keys represent bars
    '''
    def drawHistogram(self, data, label="Count", title="title"):
        
        bar_fun = plt.barh
        bar_ticks = plt.yticks
        bar_label = plt.xlabel

        n = len(data)
        bar_fun(range(n), list(data.values()), align='center', alpha=0.4)
        bar_ticks(range(n), list(data.keys()))
        bar_label(label)
        plt.title(title)
        plt.show()
