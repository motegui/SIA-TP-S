from sokoban import *


def euclidean_heuristic(position, end_position):
    return ((position[0] - end_position[0]) ** 2) + ((position[1] - end_position[1]) ** 2)


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def sokoban_heuristic(state, goal_map):
    total_distance = 0

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == BOX:
                # Encontrar la distancia mínima de la caja al objetivo correspondiente
                min_distance = float('inf')
                for k in range(len(goal_map)):
                    for l in range(len(goal_map[0])):
                        if goal_map[k][l] == '$':
                            distance = abs(i - k) + abs(j - l)
                            min_distance = min(min_distance, distance)
                total_distance += min_distance

    return total_distance