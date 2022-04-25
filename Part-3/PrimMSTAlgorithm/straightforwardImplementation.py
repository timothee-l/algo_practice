import csv

with open('input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    nodes = {}  # For each node, contains a list of edges (edges = [otherNodeId, cost])
    edges = []  # For each edge, contains [node1, node2, cost]
    firstLine = True
    n = 0  # Number of nodes
    for edge in reader:
        if firstLine:
            firstLine = False
            n = int(edge[0])  # Number of nodes
        else:
            node1 = int(edge[0])
            node2 = int(edge[1])
            cost = int(edge[2])
            edges.append([node1, node2, cost])

X = [1]  # Initialization with arbitrary node
T = []
totalCost = 0
while len(X) < n:  # While X doesn't contain all the nodes in the input graph
    lowestCost = 1000000
    cheapestEdge = -1
    toBeAddedVert = -1
    for edgeId, edge in enumerate(edges):
        node1 = edge[0]
        node2 = edge[1]
        cost = edge[2]
        if node1 in X and node2 not in X:
            if cost < lowestCost:
                lowestCost = cost
                cheapestEdge = edgeId
                toBeAddedVert = node2
        elif node1 not in X and node2 in X:
            if cost < lowestCost:
                lowestCost = cost
                cheapestEdge = edgeId
                toBeAddedVert = node1

    T.append(cheapestEdge)
    edges.pop(cheapestEdge)
    X.append(toBeAddedVert)
    totalCost += lowestCost

print(totalCost)
