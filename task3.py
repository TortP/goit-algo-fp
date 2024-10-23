import heapq

# Функція для алгоритму Дейкстри


def dijkstra(graph, start):
    # Відстані від початкової вершини до всіх інших
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Використовуємо бінарну купу для зберігання вершин
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за відому, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Побудова графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Виклик функції
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

# Виведення результатів
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")
