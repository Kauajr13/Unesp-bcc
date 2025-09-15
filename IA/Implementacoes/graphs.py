from typing import Dict, Tuple, List

Graph = Dict[str, Dict[str, float]]

def romania_graph() -> Graph:
    """Grafo de Romênia (aresta <-> custo) — valores em km conforme enunciado clássico."""
    g: Graph = {
        'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Dobreta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }
    return g

def path_cost(path: List[str], graph: Graph) -> float:
    """Retorna custo acumulado de um caminho (lista de nós)."""
    if len(path) < 2:
        return 0.0
    cost = 0.0
    for a, b in zip(path, path[1:]):
        if b in graph.get(a, {}):
            cost += graph[a][b]
        else:
            raise ValueError(f"No edge between {a} and {b}")
    return cost