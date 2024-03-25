from copy import deepcopy

from TP1.utils.state import State
from node import Node

WALL = 35
BOX = 36
EMPTY = 32


def IS_SOLID(x):
    return x == WALL or x == BOX


def IS_VERTEX(new_box_position, current_node):
    for position in [((1, 0), (0, -1)), ((-1, 0), (0, -1)), ((-1, 0), (0, 1)), ((1, 0), (0, 1))]:
        if IS_SOLID(current_node.state.current_map[new_box_position[0] + position[0][0]][new_box_position[1] + position[0][1]] and
                    IS_SOLID(current_node.state.current_map[new_box_position[0] + position[1][0]][
                                 new_box_position[1] + position[1][1]])):
            return True
    return False


def IS_WRONG_VERTEX(new_box_position, current_node):
    return IS_VERTEX(new_box_position, current_node) and new_box_position not in current_node.state.goals


def generate_children_sokoban(current_node, heuristic):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure walkable terrain
        if current_node.state.current_map[node_position[0]][node_position[1]] == WALL:
            continue
        if node_position in current_node.state.boxes:
            new_box_position = (node_position[0] + new_position[0], node_position[1] + new_position[1])
            if current_node.state.current_map[new_box_position[0]][new_box_position[1]] != EMPTY:
                continue
            if IS_SOLID(current_node.state.current_map[new_box_position[0]][new_box_position[1]]) or IS_WRONG_VERTEX(
                    new_box_position, current_node):
                continue

        new_state = generate_new_state(current_node, new_position)

        # Create new node
        new_node = Node(current_node, node_position, new_state)
        if heuristic is not None:
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_node)
            new_node.f = new_node.g + new_node.h

        # Append
        children.append(new_node)

    return children


def generate_new_state(current_node, new_position):
    new_map = deepcopy(current_node.state.current_map)
    new_boxes = deepcopy(current_node.state.boxes)
    new_map[current_node.position[0]][current_node.position[1]] = EMPTY
    state = State(new_map, current_node.state.goals, new_boxes)
    node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

    if node_position in new_boxes:
        new_map[node_position[0]][node_position[1]] = EMPTY
        new_box_position = (
            current_node.position[0] + 2 * new_position[0], current_node.position[1] + 2 * new_position[1])
        new_map[new_box_position[0]][new_box_position[1]] = BOX
        state.boxes.remove(node_position)
        state.boxes.append(new_box_position)
        state.current_map = new_map

    return state
