"""
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших 
шляхів від початкової вершини до всіх інших.
"""
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            if distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    return distances


if __name__ == "__main__":
    graph = [[(1, 4), (2, 2)], [(3, 5)], [(1, 1), (3, 8)], []]
    start_vertex = 0
    shortest_distances = dijkstra(graph, start_vertex)
    print("Найкоротші відстані від вершини", start_vertex)
    print(shortest_distances)
