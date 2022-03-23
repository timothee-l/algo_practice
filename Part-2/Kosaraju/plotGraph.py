import networkx as nx
import matplotlib.pyplot as plt

filePath = 'testCase2.txt'  # Directed graph as edge list
with open(filePath, 'rb') as read_obj:
    G = nx.read_edgelist(read_obj, create_using=nx.DiGraph)
    nx.draw(G, with_labels=True)
    plt.savefig("{}_fig.png".format(filePath))
