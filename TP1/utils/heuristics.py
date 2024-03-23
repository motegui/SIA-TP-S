from random import random
import random

BOX = '$'


def heuristic_non_admissible(state, goal_map):
    # Retorna un valor aleatorio como heurística
    return random.randint(0, 100)


def manhattan_heuristic(state, goal_map):
    total_distance = 0

    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == BOX:
                            distance = abs(x_pos_state - x_pos_goal) + abs(y_pos_state - y_pos_goal)
                            min_distance = min(min_distance, distance)
                total_distance += min_distance

    return total_distance


def euclidean_heuristic(state, goal_map):
    total_distance = 0
    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == BOX:
                            distance = (x_pos_state - x_pos_goal) ** 2 + (y_pos_state - y_pos_goal) ** 2
                            min_distance = min(min_distance, distance)
                total_distance += min_distance

    return total_distance
