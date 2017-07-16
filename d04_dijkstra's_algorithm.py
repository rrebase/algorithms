# Dijkstra's algorithm - finding the shortest paths between nodes in a graph
# visualization https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html

# dictionary representations of graph
graph1 = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

graph2 = {
    '0': {'2': 5, '1': 5, '3': 1},
    '2': {'4': 5, '6': 7, '5': 9, '1': 4, '0': 5},
    '3': {'1': 7, '0': 1, '5': 6},
    '4': {'2': 5, '6': 6},
    '5': {'7': 6, '3': 6, '2': 9},
    '6': {'4': 6, '2': 7},
    '7': {'5': 6}
}


def dijkstra(graph, current):  # starting node

    unvisited = {node: float("inf") for node in graph.keys()}  # by default all nodes are unreachable
    visited = {}
    currentDistance = 0

    while True:
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited:  # have already visited
                continue
            newDistance = currentDistance + distance
            unvisited[neighbour] = min(unvisited[neighbour], newDistance)
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:  # empty
            break
        # set current node as the one with minimum distance
        current, currentDistance = sorted(unvisited.items(), key=lambda x: x[1])[0]
    return visited


print(dijkstra(graph1, 'B'))  # -> {'B': 0, 'D': 1, 'G': 2, 'E': 2, 'C': 3, 'A': 4, 'F': 4}
print(dijkstra(graph2, '7'))  # -> {'7': 0, '5': 6, '3': 12, '0': 13, '2': 15, '4': 20, '6': 22}
