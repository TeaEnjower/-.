def dijkstra(graph, start, stop = False):
    distances = {v: float('infinity') for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    parents = {v: None for v in graph}

    while queue:
        current_distance, current_vertex = min(queue, key=lambda x: x[0])
        queue.remove(min(queue, key=lambda x: x[0]))

        # Обрабатываем только вершину с наименьшим расстоянием
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
                parents[neighbor] = current_vertex

    if stop:
        return distances[stop], PATH(stop, parents)

    return distances, parents


def BellmanFord(graph, start, stop=False): 

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
					print("Существует отрицательный цикл")
	if stop:
		return dist[stop], PATH(stop, parents)
	return dist, parents

graph = {
    't': {9: 9},
    9: {5: 5, 7: 7},
    5: {4: 4, 6: 6},
    7: {6: 6, 8: 8},
    8: {14: 14, 's': 8},
    4: {3: 3, 13: 13},
    3: {1: 1, 12: 12},
    1: {2: 2, 's': 1},
    2: {10: 10, 11: 11},
    6: {'s': 6},
    14: {},
    13: {},
    11: {},
    10: {},
    12: {},
    's': {}
}
#получаются совершенно аналогичные ответы, значит всё работает правильно)
print(dijkstra(graph, 't', 's'))
print(BellmanFord(graph, 't', 's'))

