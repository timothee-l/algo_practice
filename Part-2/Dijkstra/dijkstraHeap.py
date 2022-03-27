import heapq as hq
import csv

# Input : undirected weighted graph; 200 vertices labeled 1 to 200.
# Each row consists of the node tuples adjacent to that particular vertex along with the length of that edge
n = 200

with open('dijkstraData.txt', 'r') as read_obj:
    csvReader = csv.reader(read_obj, delimiter='\t')
    rawGraph = list(csvReader)
    rows = [[[int(x[0]), int(x[1])] for x in (item.split(",") for item in row[1:-1])] for row in rawGraph]
    graph = {k: v for (k, v) in zip(range(1, 201), rows)}

shortestPath = {1: 0}  # Length of the shortest pass from s (labelled 1) to v (labelled key)


def createHeap():
    # Heap contains the greedy criterion for an edge and the label of it's head vertex
    heap = []
    for k, v in graph.items():
        if k in shortestPath:
            continue  # Ignoring starting vertex
        bestScore = 1000000
        for (w, length) in v:
            if w in shortestPath:
                greedyScore = shortestPath[w] + length
                if greedyScore < bestScore:
                    bestScore = greedyScore
        hq.heappush(heap, (bestScore, k))  # bestScore used as heap
    return heap


def dijkstra():
    heap = createHeap()
    for _ in range(n - 1):  # For every vertex in graph (other than starting vertex 1)
        greedyScore, w = hq.heappop(heap)  # Next vertex to be processed
        shortestPath[w] = greedyScore
        for [v, length] in graph[w]:  # Finds the new crossing edges (with v as head) and re-evaluates greedy criterion
            if v not in shortestPath:
                for item in heap:  # TODO : improvement : keeping track of priority instead ?
                    if item[1] == v:
                        oldScore = item[0]
                        heap.remove(item)
                        hq.heapify(heap)
                        newScore = min(oldScore, greedyScore + length)
                        hq.heappush(heap, (newScore, v))


dijkstra()
outputVertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
output = []
for key in outputVertices:
    output.append(shortestPath[key])
print(output)
