import csv

with open('clustering_big.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    nodes = {}  # For each node, contains a list of edges (edges = [otherNodeId, cost])
    n = 0  # Number of nodes
    b = 0  # Number of bits for Hamming distance
    for nodeNum, node in enumerate(reader, -1):
        if nodeNum == -1:
            n = int(node[0])  # Number of nodes
            b = int(node[1])
        else:
            nodes[nodeNum] = sum([int(bit) * 2 ** power for power, bit in enumerate(node[:-1])])

# Initialization : n clusters of size 1 leaded by their single node
# All clusters will be numbered by their leading vertex (the initial vertex it contains)
parent = {i: i for i in range(n)}  # Parent node of given vertex
clusters = set(range(n))


# Finds leading vertex of given vertex
def find(u):
    v = parent[u]
    while u != v:
        u = v
        v = parent[u]
    return v


# Merge clusters c and d
def union(i, j):
    parent[i] = j
    clusters.remove(i)


def hamming(i, j):
    N = i ^ j
    return countSetBits(N)


def countSetBits(N):
    count = 0
    while N:
        count += N & 1
        N >>= 1
    return count


def SlcBig():
    for u, uBits in nodes.items():
        for v, vBits in nodes.items():
            cost = hamming(uBits, vBits)
            if 0 < cost < 3:  # Only merge if cost < 3 (also checks for u not being v)
                x, y = find(u), find(v)
                if x != y:  # Only merge different clusters
                    union(x, y)
    return len(clusters)


print(SlcBig())
