import csv

k = 4  # Target number of clusters

with open('clustering1.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    edgeCost = {}  # For each node, contains a list of edges (edges = [otherNodeId, cost])
    edgeNodes = {}  # For each edge, contains [node1, node2, cost]
    n = 0  # Number of nodes
    for edgeNum, edge in enumerate(reader, -1):
        if edgeNum == -1:
            n = int(edge[0])  # Number of nodes
        else:
            node1 = int(edge[0]) - 1
            node2 = int(edge[1]) - 1
            cost = int(edge[2])
            edgeCost[edgeNum] = cost
            edgeNodes[edgeNum] = node1, node2

# Initialization : n clusters of size 1 leaded by their single node
# All clusters will be numbered by their leading vertex (the initial vertex it contains)
parent = {i: i for i in range(n)}  # Parent node of u
size = {i: 1 for i in range(n)}  # Size of cluster c


# Finds leading vertex of given vertex
def find(u):
    v = parent[u]
    while u != v:
        u = v
        v = parent[u]
    return v


# Merge clusters c and d
def union(c, d):
    if size[c] < size[d]:
        S = c  # Smaller cluster
        L = d  # Larger cluster
    else:
        S = d
        L = c

    # leadS = leader[S]
    # leadL = leader[L]

    # parent[leadS] = leadL
    parent[S] = L
    size[L] += size[S]

    size.pop(S)
    # leader.pop(S)


def singleLinkClustering():
    while len(size) > k:  # While still too many clusters
        e = min(edgeCost, key=edgeCost.get)  # Edge with minimum cost
        u, v = [find(i) for i in edgeNodes[e]]  # Cluster leaders / Cluster numbers for nodes of e
        edgeCost.pop(e)
        edgeNodes.pop(e)
        if u == v:
            continue  # Nodes in same cluster
        union(u, v)  # Merging the two clusters

    while True:
        e = min(edgeCost, key=edgeCost.get)  # Edge with minimum cost
        u, v = [find(i) for i in edgeNodes[e]]  # Cluster leaders / Cluster numbers for nodes of e
        if u == v:
            edgeCost.pop(e)
            edgeNodes.pop(e)
        else:
            return edgeCost[e]


print(singleLinkClustering())
