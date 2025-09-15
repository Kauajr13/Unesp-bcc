from graphs import romania_graph, path_cost
from heuristics import h
from a_star import a_star_search
from greedy import greedy_best_first_search

def show_result(name, path, cost, explored):
    print(f"--- {name} ---")
    if path is None:
        print("No path found.")
    else:
        print("Path:", " -> ".join(path))
        print("Cost:", cost)
    print("Explored order (first 20):", explored[:20])
    print()

def main():
    graph = romania_graph()
    start = 'Arad'
    goal = 'Bucharest'

    path_a, cost_a, explored_a = a_star_search(graph, start, goal, h)
    show_result("A* Search", path_a, cost_a, explored_a)

    path_g, cost_g, explored_g = greedy_best_first_search(graph, start, goal, h)
    show_result("Greedy Best-First Search", path_g, cost_g, explored_g)

if __name__ == "__main__":
    main()
