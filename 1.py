def bfs(graph, start):
    """Perform Breadth-First Search traversal on the given graph."""
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)



graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

print(bfs(graph, 'A'))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)



graph = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0'],
    '3': ['1'],
    '4': ['2', '3']
}

dfs(graph, '0')