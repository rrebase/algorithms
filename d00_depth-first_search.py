# Depth-first search algorithm

# dictionary representation of a graph
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
    for i in graph[node]:
        if i not in visited:
            dfs(i)
    return path

print(dfs('A'))  # out -> ['A', 'Z', 'C', 'D', 'B', 'F', 'G', 'Y']
