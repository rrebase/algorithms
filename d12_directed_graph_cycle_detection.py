# Algorithm for cycle detection in directed graphs
# Graphs with dictionaries mapping vertices to neighbouring vertices

g1 = {
    1: [2],
    2: [3],
    3: [1]
}

g2 = {1: [1]}

g3 = {
    1: [2, 3, 4],
    2: [3, 4],
    3: [4]
}

path, visited = [], []

def visit(graph, node):
    """Return True if the node is in a cycle."""
    if node in visited:
        return False
    path.append(node)
    visited.append(node)
    for neighbour in graph.get(node, []):
        if neighbour in path or visit(graph, neighbour):
            return True
    path.remove(node)
    return False

def cyclic(graph):
    """Return True if the graph has a cycle."""
    return any(visit(graph, v) for v in graph)

print(cyclic(g1))  # -> True
print(cyclic(g2))  # -> True
print(cyclic(g3))  # -> False
