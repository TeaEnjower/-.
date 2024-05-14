def BellmanFord(graph, start): 

	dist = {v: float('infinity') for v in graph}
	dist[start] = 0
	parents = {v: None for v in graph}

	for n in range(len(graph)):
		for i in graph:
			for neighbor, w in graph[i].items():
				if dist[i] != float("Inf") and dist[i] + w < dist[neighbor]: 
					dist[neighbor] = dist[i] + w
					parents[neighbor] = i


	for i in graph:
		for neighbor, w in graph[i].items():
			if dist[i] != float("Inf") and dist[i] + w < dist[neighbor]: 
					print ("Существует отрицательный цикл")
						
	return  dist, parents

def PATH (end, parents):
    path = [end]
    parent = parents[end]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 3, 'B': 2}
}
BellmanFord(graph, 'A')