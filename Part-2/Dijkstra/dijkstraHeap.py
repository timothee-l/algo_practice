import heapq as hq
import csv

# Input : undirected weighted graph; 200 vertices labeled 1 to 200.
# Each row consists of the node tuples adjacent to that particular vertex along with the length of that edge
n = 200

with open('dijkstraData.txt', 'r') as read_obj:
    csvReader = csv.reader(read_obj, delimiter='\t')
    rawGraph = list(csvReader)
    rows = [[[int(x[0]), int(x[1])] for x in (item.split(",") for item in row[1:-1])] for row in rawGraph]
    G = {k: v for (k, v) in zip(range(1, 201), rows)}


def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue  # Already encountered before
        # We know that this is the first time we encounter node.
        #   As we pull nodes in order of increasing distance, this
        #   must be the node's shortest distance from the start node.
        distances[node] = dist
        for neighbor, weight in graph[node]:
            if neighbor not in distances:
                hq.heappush(heap, (dist + weight, neighbor))

    return distances


shortestPath = dijkstra(G, 1)
outputVertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
output = []
for key in outputVertices:
    output.append(shortestPath[key])
print(output)
