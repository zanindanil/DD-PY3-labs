from typing import List
import heapq


def min_cost_stairs(costs: List[int]) -> int:
    # Создаем граф в виде словаря, где ключи - номера ступеней, значения - список соседних ступеней и их стоимостей
    graph = {}
    n = len(costs)

    # Добавляем начальную ступень (землю) в граф
    graph[0] = [(1, costs[0])]  # Переход с земли на первую ступень

    # Добавляем промежуточные ступени в граф
    for i in range(1, n - 1):
        graph[i] = [(i + 1, costs[i]), (i + 2, costs[i])]  # Переход на следующую ступень или перепрыгивание через одну

    # Добавляем последнюю ступень в граф
    graph[n - 1] = [(n, costs[n - 1])]  # Переход на последнюю ступень

    # Используем алгоритм Дейкстры для нахождения кратчайшего пути
    distances = {i: float('inf') for i in range(n + 1)}  # Инициализируем все расстояния как бесконечность
    distances[0] = 0  # Расстояние от начальной ступени (земли) до нее самой равно 0
    priority_queue = [(0, 0)]  # Очередь с приоритетом для обработки ступеней

    while priority_queue:
        current_dist, current_stair = heapq.heappop(priority_queue)

        # Если достигли последней ступени, возвращаем наименьшую сумму
        if current_stair == n:
            return current_dist

        # Просматриваем соседние ступени текущей ступени
        for neighbor, cost in graph[current_stair]:
            distance = current_dist + cost

            # Если найденное расстояние до соседней ступени меньше сохраненного, обновляем его и добавляем в очередь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1  # Если не удалось достичь последней ступени