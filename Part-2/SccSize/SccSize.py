import csv, threading, sys

sys.setrecursionlimit(800000)
threading.stack_size(67108864)
# Goal : compute SCCs and return size of the nScc largest SCCs

# TEST : 6,3,2,1,0
nScc = 5  # Number of strongly connected components necessary (nScc largest)
n = 12  # 875714  # Number of nodes in input graph
m = 20  # 5105042  # Number of edges in input graph

# input : directed graph, vertices labelled 1 to 875714
# row : edge from first vertex to second vertex
with open('testCase.txt', 'r') as read_obj:
    csvReader = csv.reader(read_obj, delimiter=' ')
    graph = list(csvReader)
    graph = tuple([[vert for vert in row if vert != ''] for row in graph])

t = 0  # keeps count of the number of nodes processed
s = None  # keeps track of the current source vertex
explored = [1] * n  # Vertices "explored" have value 0 (vertices indexed by label)
leader = [0] * n  # Gives "leading" vertex for each vertex (vertices indexed by label)
finishingTime = [0] * n  # Values are the "finishing" time of each vertex (vertices indexed by label)
leaderCount = {}  # Counts vertices leaded by given vertex (vertices indexed by label)


# Input is a graph G containing n nodes, m vertices
# Computes SCCs of given graph using a leading vertex for each SCC
def DFSLoop(G):
    global explored
    global leader
    global t
    global s
    t = 0
    s = None
    for i in reversed(range(n)):
        if explored[i] == 1:
            s = i
            leaderCount[i] = 0
            DFS(G, i)
            print(i)


# Depth first search in graph G from starting vertex i (edges reversed)
def DFS(G, i):
    global t
    global s
    global explored
    global leader
    global finishingTime
    explored[i] = 0
    leader[i] = s
    leaderCount[s] = leaderCount.get(s) + 1

    for e in G:
        v = e[0]  # Edges NOT reversed
        if v == i:
            w = e[1]
            if explored[w] == 1:
                DFS(G, w)
    t += 1
    finishingTime[i] = t


# Depth first search in graph G from starting vertex i (edges reversed)
def DFS2(G, i, step):
    global t
    global s
    global explored
    global leader
    global finishingTime
    explored[i] = 0
    leader[i] = s
    leaderCount[s] = leaderCount.get(s) + 1

    if step == 1:
        for e in G:
            v = e[1]  # Edges reversed
            if v == i:
                w = e[0]
                if explored[w] == 1:
                    DFS(G, w)
        t += 1
        finishingTime[i] = t
    else:  # Step is 2
        for e in G:
            v = e[0]
            if v == finishingTime[i]:
                w = e[1]
                if explored[w] == 1:
                    DFS(G, w)
        t += 1
        finishingTime[i] = t


def computeSCC(G=graph):
    DFSLoop(G)

    # Count size of nScc-largest SCCs
    print("Leaders of biggest SCCs (by descending order)")
    for k in range(0, nScc):
        max_value = max(leaderCount.values())
        max_key = max(leaderCount, key=leaderCount.get)
        leaderCount.pop(max_key)
        print("Leading vertex : {}, Size of SCC : {}".format(max_key, max_value))


thread = threading.Thread(target=computeSCC)
thread.start()
