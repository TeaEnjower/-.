def dijkstra(graph, start, stop = False):
    distances = {v: float('infinity') for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    processed = set()
    parents = {v: None for v in graph}

    while queue:
        current_distance, current_vertex = min(queue, key=lambda x: x[0])
        processed.add(current_vertex)
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

        if stop and all(n in processed for n in graph[stop].keys()):
            return distances[stop], parents

        

    return distances, parents


def PATH (end, parents):
    path = [end]
    parent = parents[end]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]