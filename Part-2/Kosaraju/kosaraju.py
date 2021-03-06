import csv
import sys
import threading
import timeit

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

# Goal : compute SCCs with Kosaraju's Algorithm and return size of the nScc largest SCCs
start = timeit.default_timer()
nScc = 5  # Number of strongly connected components necessary (nScc largest)
n = 875714  # Number of nodes in input graph
m = 5105042  # Number of edges in input graph

# input : directed graph, vertices labelled 1 to 875714
# row : edge from first vertex to second vertex
with open('input.txt', 'r') as read_obj:
    csvReader = csv.reader(read_obj, delimiter=' ')
    G = list(csvReader)
    G = tuple([[int(vert) for vert in row if vert != ''] for row in G])

t = 0  # keeps count of the number of nodes processed
s = None  # keeps track of the current source vertex
# Bitset à la place d'int
explored = [1] * n  # Vertices "explored" have value 0 (vertices indexed by label)
leader = [0] * n  # Gives "leading" vertex for each vertex (vertices indexed by label)
finishingTime = [0] * n  # Returns finishing time associated to vertex label index
finishingTimeVert = [0] * n  # Inverse of finishingTime
leaderCount = {}  # Counts vertices leaded by given vertex (vertices indexed by label)

RAL1 = {}
RAL2 = {}


# Input is a graph G containing n nodes, m vertices
# Computes SCCs of given graph using a leading vertex for each SCC
def DFSLoop(lapse=0):
    global explored
    global t
    global s
    t = 0
    s = None
    explored = [1] * n
    i = n
    while i > 0:
        i -= 1
        if explored[i] == 1:
            if lapse == 2:
                s = i
                DFS2(i)
            else:  # Lapse == 1
                DFS1(i)


# Depth first search in graph G from starting vertex i
def DFS(i):
    global explored
    explored[i] = 0
    for e in G:
        v = e[0] - 1  # vertex labels start at 1 in graph but python lists at index 0
        if v == i:
            w = e[1] - 1
            if explored[w] == 1:
                DFS(w)


# Lapse 1 DFS
def DFS1(i):
    global t
    global explored
    global finishingTimeVert
    global finishingTime
    explored[i] = 0
    if (i+1) in RAL1:
        for w in RAL1[i + 1]:
            w -= 1
            if explored[w] == 1:
                DFS1(w)
    finishingTimeVert[t] = i
    finishingTime[i] = t
    t += 1


def DFS2(i):
    global explored
    global leader
    explored[i] = 0
    leader[finishingTimeVert[i]] = finishingTimeVert[s]
    leaderCount[finishingTimeVert[s]] = leaderCount.get(finishingTimeVert[s], 0) + 1
    if (finishingTimeVert[i]+1) in RAL2:
        for w in RAL2[finishingTimeVert[i]+1]:
            w -= 1
            if explored[finishingTime[w]] == 1:
                DFS2(finishingTime[w])


def main():
    print("Start")
    # 1. DFSLoop(G [edges reversed])
    for e in G:
        if e[1] not in RAL1:
            RAL1[e[1]] = [e[0]]
        else:
            RAL1[e[1]].append(e[0])
        if e[0] not in RAL2:
            RAL2[e[0]] = [e[1]]
        else:
            RAL2[e[0]].append(e[1])
    DFSLoop(1)  # OK
    print("Lapse 1 Done")
    # 2. DFSLoop(G [vertex labelled as finishing times])
    DFSLoop(2)
    # Size of largest SCCs
    out = ''
    k = 0
    while leaderCount and k < nScc:
        k += 1
        max_value = max(leaderCount.values())
        max_key = max(leaderCount, key=leaderCount.get)
        out += str(max_value) + ' '
        leaderCount.pop(max_key)
    stop = timeit.default_timer()
    print(stop - start) # 11 seconds


thread = threading.Thread(target=main)
thread.start()
# main()
