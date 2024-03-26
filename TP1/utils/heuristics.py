from random import random
import random


def rand_heuristic(state):
    # Retorna un valor aleatorio como heurística
    return random.randint(0, 100)


def player_movements_heuristic(current_node):
    total_distance = 0
    min_box_player_distance = float('inf')
    last_goal = None
    for box in current_node.state.boxes:
        box_player_distance = manhattan_distance(box, current_node.position)
        min_box_player_distance = min(min_box_player_distance, box_player_distance)
        min_box_goal_distance = float('inf')
        for goal in current_node.state.goals:
            box_goal_distance = manhattan_distance(box, goal)
            if min_box_goal_distance > box_goal_distance:
                last_goal = goal
                min_box_goal_distance = box_goal_distance
        total_distance += min_box_goal_distance
        if last_goal is None:
            total_distance += manhattan_distance(box, current_node.position)
        else:
            total_distance += manhattan_distance(box, last_goal)
    return total_distance


def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def manhattan_heuristic(current_node):
    total_distance = 0
    for box in current_node.state.boxes:
        if box not in current_node.state.goals:
            min_box_goal_distance = float('inf')
            for goal in current_node.state.goals:
                if goal not in current_node.state.boxes:
                    box_goal_distance = manhattan_distance(box, goal)
                    min_box_goal_distance = min(min_box_goal_distance, box_goal_distance)

            total_distance += min_box_goal_distance
    return total_distance


def euclidean_distance(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5


def euclidean_heuristic(current_node):
    total_distance = 0
    for box in current_node.state.boxes:
        min_box_goal_distance = float('inf')
        for goal in current_node.state.goals:
            box_goal_distance = euclidean_distance(box, goal)
            min_box_goal_distance = min(min_box_goal_distance, box_goal_distance)
        total_distance += min_box_goal_distance
    return total_distance
