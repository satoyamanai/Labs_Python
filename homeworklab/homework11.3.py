import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Очередь для посещения вершин

    while queue:
        vertex = queue.popleft()  # Берем первую вершину из очереди
        if vertex not in visited:
            print("Visiting:", vertex)
            visited.add(vertex)

            plt.clf()
            nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=20, font_weight="bold")  # Рисуем граф
            nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color="lightgreen", node_size=1500)
            nx.draw_networkx_edges(G, pos, edgelist=[(start, vertex) for start in visited], edge_color="red", width=2)
            plt.title("BFS: Visiting " + vertex)
            plt.pause(1)

            # Добавляем соседние вершины в очередь
            queue.extend(graph[vertex])

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

G = nx.DiGraph(graph)

pos = nx.spring_layout(G)

start_vertex = 'A'
bfs_result = bfs(graph, start_vertex)

plt.show()