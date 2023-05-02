"""Module that contains the floyd_warshall all pairs shortest path implementation"""
import json
import itertools

DIFFERENCE_FROM_0_TO_A_IN_ASCII: int = 96
INT_MAX_SIZE: int = 100000


def convert_letter_to_number(letter: str) -> int:
    """Takes in a letter and uses ASCII ordering to convert it
    to its 1-indexed placement in the alphabet"""
    cpy: str = letter.lower()
    number: int = ord(cpy) - DIFFERENCE_FROM_0_TO_A_IN_ASCII
    return number


def floyd_warshall(graph: dict[str, dict[str, int]]) -> list[list[int]]:
    """Receives a graph and returns a matrix of sum weight of travelling between nodes"""
    distances: list[list[int]] = [
        list(itertools.repeat(INT_MAX_SIZE, len(graph))) for x in graph
    ]
    # Initialize all nodes with their edges' weights
    for key, values in graph.items():
        for key2, value2 in values.items():
            distances[convert_letter_to_number(key) - 1][
                convert_letter_to_number(key2) - 1
            ] = value2

    # Initialize all nodes weight to themselves to 0
    for key, values in graph.items():
        distances[convert_letter_to_number(key) - 1][
            convert_letter_to_number(key) - 1
        ] = 0

    # If the distance between nodes 'i' and 'j' would be shorter
    # through a third node k, then use that as the route.
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances


def main() -> None:
    """Function main, runs the module"""
    with open("./graphs/A-E.json", "r", encoding="utf-8") as read_file:
        graph_a_to_e: dict[str, dict[str, int]] = json.load(read_file)
    print(floyd_warshall(graph_a_to_e))
    with open("./graphs/A-G.json", "r", encoding="utf-8") as read_file:
        graph_a_to_g: dict[str, dict[str, int]] = json.load(read_file)
    print(floyd_warshall(graph_a_to_g))
    with open("./graphs/A-O.json", "r", encoding="utf-8") as read_file:
        graph_a_to_o: dict[str, dict[str, int]] = json.load(read_file)
    print(floyd_warshall(graph_a_to_o))


if __name__ != "main":
    main()
