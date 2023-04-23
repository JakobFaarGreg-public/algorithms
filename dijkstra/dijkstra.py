"""Module that contains the dijkstra's shortest path implementation"""
import json

def dijkstra(
    graph: dict[str, dict[str, int]], source: str
) -> dict[str, tuple[int, str]]:
    """Receives a graph and a starting node, returns a table of shortest paths and previous nodes"""
    unvisited_nodes: list[str] = []
    shortest_path: dict[str, tuple[int, str]] = {}
    for key in graph:
        unvisited_nodes.append(key)
        if key != source:
            shortest_path[key] = (1000, "null")
        else:
            shortest_path[key] = (0, "source")
    while len(unvisited_nodes) != 0:
        selected_node: str = find_smallest_distance(shortest_path, unvisited_nodes)
        unvisited_nodes.remove(selected_node)
        shortest_path = update_shortest_path(
            selected_node, graph[selected_node], shortest_path
        )
    return shortest_path


def find_smallest_distance(
    shortest_path: dict[str, tuple[int, str]], unvisited_nodes: list[str]
) -> str:
    """Finds the unvisited node with the least distance from source node"""
    minimum: int = 1000
    smallest: str = "null"
    for elem in unvisited_nodes:
        if shortest_path[elem][0] < minimum:
            minimum = shortest_path[elem][0]
            smallest = elem
    return smallest


def update_shortest_path(
    source: str, neighbors: dict[str, int], shortest_path: dict[str, tuple[int, str]]
) -> dict[str, tuple[int, str]]:
    """Updates shortest path thrugh some given source node"""
    for key, value in neighbors.items():
        if value + shortest_path[source][0] < shortest_path[key][0]:
            shortest_path[key] = value + shortest_path[source][0], source
    return shortest_path


def main() -> None:
    """Function main, runs the module"""
    with open("./graphs/A-E.json", "r", encoding="utf-8") as read_file:
        data_a_e: "dict[str,dict[str,int]]" = json.load(read_file)
    print(dijkstra(data_a_e, "A"))
    with open("./graphs/A-G.json", "r", encoding="utf-8") as read_file:
        data_a_g: "dict[str,dict[str,int]]" = json.load(read_file)
    print(dijkstra(data_a_g, "A"))
    with open("./graphs/A-O.json", "r", encoding="utf-8") as read_file:
        data_a_o: "dict[str,dict[str,int]]" = json.load(read_file)
    print(dijkstra(data_a_o, "A"))


if __name__ != "main":
    main()
