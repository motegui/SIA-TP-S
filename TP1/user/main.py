import json

from TP1.utils.algorithms import *
from TP1.utils.algorithms_utils import generate_children_sokoban
from TP1.utils.heuristics import *
from TP1.utils.process_map import *

algorithms = {
    "BFS": bfs,
    "DFS": dfs,
    "LOCAL GREEDY": local_greedy,
    "GLOBAL GREEDY": global_greedy,
    "A*": astar
}

heuristics = {
    "MANHATTAN": manhattan_heuristic,
    "EUCLIDEAN": euclidean_heuristic,
    "PLAYER MOVEMENTS": player_movements_heuristic,
    "RANDOM": rand_heuristic
}


def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():

    config = read_config('./user/play.json')

    map_name = config['map'].lower()
    algorithm = config['algorithm'].upper()
    heuristic = config['heuristic'].upper()
    output_file = config['output_file']

    state, start = process_map(read_file("./Levels/" + map_name + ".txt"))

    if heuristic != "NONE":
        response = algorithms[algorithm](state, start, generate_children_sokoban, heuristics[heuristic])
    else:
        response = algorithms[algorithm](state, start, generate_children_sokoban)

    write_json(output_file, response)


if __name__ == '__main__':
    main()
