# Input :
# Undirected graph represented as adjacency list
# 200 vertices, labeled 1 to 200 in first column
# Later columns indicate all adjacent vertices and indexes (ends with None)
# ---
# Goal :
# Implement randomized contraction algorithm for the min cut problem
# (and compute min cut for given graph)
# ---
# Hint :
# Have to figure out an implementation of edge contraction
# + think about more space-efficicient implementation

import csv
import random
import math

with open('kargerMinCut.txt', 'r') as read_obj:
    csvReader = csv.reader(read_obj, delimiter='\t')
    graph = list(csvReader)
    # Removing None values + Convert to integers
    graph = [[int(vert) for vert in sublist if vert != ''] for sublist in graph]


def RCA():
    G = graph.copy()
    n = len(G)
    while n > 2:
        # Randomly choosing two vertices (and their index)
        iv1 = random.randint(0, n - 1)

        v1 = G[iv1][0]
        v2 = random.choice(G[iv1][1:])
        iv2 = None
        for index, sublist in enumerate(G):
            if sublist[0] is v2:
                iv2 = index

        # Graph Contraction (v1 and v2 merged, v1 becomes the merged vertex)
        G[iv2] = [i for i in G[iv2] if i != v1]
        G[iv1] = [i for i in G[iv1] if (i != v2) and (i > 0)]
        # Removing self-loops
        G[iv1] += G[iv2][1:]  # Vertices adjacent to v2 now adjacent to v1 (1/2)
        del G[iv2]
        n -= 1
        for i in range(n):
            if G[i][0] is not v1:
                G[i] = [v1 if vert is v2 else vert for vert in G[i]]  # (2/2)
    return len(G[1])


def main():
    crossingEdges = len(graph)  # Upper bound for min cut's crossing edges
    N = int((len(graph) ** 2) * math.log(len(graph)))  # 1-(1/n) chance of success
    for k in range(N):
        kCut = RCA()
        if k % 4 == 0:
            print("k=", k, "  crossingEdges=", crossingEdges)
        if kCut < crossingEdges:
            crossingEdges = kCut
    print("Min cut found has " + str(crossingEdges) + " crossing edges.")
    print("Accuracy is " + str(100 * (1 - (1 / len(graph)))) + "%")


if __name__ == "__main__":
    main()
