# Breadth-first search algorithm

# dictionary representations of graph
graph = {
    'A': ['Z'],
    'Z': ['C', 'Y'],
    'C': ['D', 'F'],
    'D': ['B'],
    'F': ['G'],
}


# visits all the nodes of a graph (connected component) using BFS
def bfs(start):  # start node
    visited = []  # keep track of all visited nodes
    queue = [start]  # keep track of nodes to be checked

    # keep looping until there are nodes still to be checked
    while queue:
        node = queue.pop(0)  # pop first node from queue
        if node not in visited:
            visited.append(node)  # add node to list of visited nodes
            if node not in graph:
                continue
            neighbours = graph[node]
            for neighbour in neighbours:  # add neighbours of node to queue
                queue.append(neighbour)
    return visited


print(bfs('A'))  # -> ['A', 'Z', 'C', 'Y', 'D', 'F', 'B', 'G']
