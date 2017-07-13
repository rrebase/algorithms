# Depth-first search bonus

# adjacency list representation
graph = [
    [3, 5],
    [2, 3, 4],
    [1, 5],
    [1, 0],
    [1],
    [2, 0]
]

path, visited = [], []


def dfs(node):  # starting node
    path.append(node)
    visited.append(node)
    if node > len(graph) - 1:
        return
    for j in graph[node]:
        if j not in visited:
            dfs(j)
    return path


print(dfs(0))  # out -> [0, 3, 1, 2, 5, 4]
