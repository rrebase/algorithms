# Depth-first search algorithm

# dictionary representations of graph
graph = {
    'A': ['Z'],
    'Z': ['C', 'Y'],
    'C': ['D', 'F'],
    'D': ['B'],
    'F': ['G'],
}

visited, path = [], []


def dfs(node):  # starting node
    path.append(node)
    visited.append(node)
    if node not in graph:
        return
    for neighbour in graph[node]:  # call dfs with every neighbour node
        if neighbour not in visited:
            dfs(neighbour)
    return path

print(dfs('A'))  # out -> ['A', 'Z', 'C', 'D', 'B', 'F', 'G', 'Y']
