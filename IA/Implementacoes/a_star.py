import heapq
from typing import Dict, Tuple, List, Callable, Optional
from graphs import Graph, path_cost

def a_star_search(graph: Graph, start: str, goal: str, h: Callable[[str], float]):
    """
    A* search returning (path, cost, explored_order)
    - path: lista de nós do start ao goal (ou None se não encontrado)
    - cost: custo do caminho (float) ou float('inf') se não encontrado
    - explored_order: nó por nó na ordem em que foram retirados da frontier
    """
    frontier = []
    heapq.heappush(frontier, (h(start), 0.0, start))  # (f = g+h, g, node)
    came_from: Dict[str, Optional[str]] = {start: None}
    g_score: Dict[str, float] = {start: 0.0}
    explored_order: List[str] = []

    while frontier:
        f, g, current = heapq.heappop(frontier)
        explored_order.append(current)
        if current == goal:
            # reconstruir caminho
            path = []
            n = current
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()
            return path, g_score[current], explored_order

        for neighbor, cost in graph.get(current, {}).items():
            tentative_g = g_score[current] + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)
                heapq.heappush(frontier, (f_score, tentative_g, neighbor))

    return None, float('inf'), explored_order