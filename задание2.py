graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 3, 'B': 2}
}

a, b = dijkstra(graph, 'A')
path = PATH('C', b)
path2 = set()

for i in range(len(path)-1):
    path2.add((path[i], path[i+1]))

