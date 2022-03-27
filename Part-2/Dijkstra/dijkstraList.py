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


# Computes Dijkstra greedy criterion for all crosing edges and outputs the best result (length and edge's head vertex)
def greedyCriterion():
    minLength = 1000000
    head = None
    for k in shortestPath.keys():  # Edge starting from already processed vertex
        for (vert, length) in graph[k]:
            if vert not in shortestPath:  # Edge leading to unprocessed vertex
                criterion = shortestPath[k] + length
                if minLength > criterion:  # Dijkstra Greedy Criterion
                    minLength = criterion
                    head = vert
                if head is None:
                    head = vert  # Guarantees picking an unconnected vertex if the connected part of the graph has
                    # been fully explored already
    return minLength, head


for _ in range(n - 1):  # For every vertex in graph (other than starting vertex 1)
    # Computes next to be added vertex
    pathLength, vert = greedyCriterion()
    # Add the vertex, and its shortest path to the dictionary
    shortestPath[vert] = pathLength

outputVertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
output = []
for key in outputVertices:
    output.append(shortestPath[key])
print(output)
