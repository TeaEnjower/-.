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