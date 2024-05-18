import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 3},
    'C': {'A': 3, 'B': 2, 'D': 4},
    'D': {'B': 3, 'C': 4}
}

start_node = 'A'

shortest_paths = dijkstra(graph, start_node)

print("from point", start_node, "to other points that shortest path：")
for node, distance in shortest_paths.items():
    print(f"arrive to point {node} that distance is: {distance}")
