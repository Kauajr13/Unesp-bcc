import heapq
from typing import Dict, Tuple, List, Callable
from graphs import Graph, path_cost

def greedy_best_first_search(graph: Graph, start: str, goal: str, h: Callable[[str], float]):
    """
    Greedy Best-First Search:
    - Expande nós ordenando apenas por h(n) (não considera g).
    Retorna (path, cost, explored_order).
    """
    frontier = []
    heapq.heappush(frontier, (h(start), start))
    came_from: Dict[str, str] = {start: None}
    explored_order: List[str] = []
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        explored_order.append(current)

        if current == goal:
            # reconstruir caminho
            path = []
            n = current
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()
            return path, path_cost(path, graph), explored_order

        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(frontier, (h(neighbor), neighbor))

    return None, float('inf'), explored_order
