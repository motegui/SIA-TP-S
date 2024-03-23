from copy import deepcopy

WALL = '#'
BOX = '$'
EMPTY = ' '


def IS_SOLID(x):
    return x == '#' or x == '$'


class Node:
    def __init__(self, parent=None, position=None, state=None):
        self.parent = parent
        self.position = position
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return all([a == b for a, b in zip(self.state, other.state)]) and self.position == other.position

    def map_equals(self, other):
        return all([a == b for a, b in zip(self.state, other.state)])


def generate_new_state(current_node, new_position):
    new_map = deepcopy(current_node.state)
    new_map[current_node.position[0]][current_node.position[1]] = EMPTY

    if new_map[current_node.position[0] + new_position[0]][current_node.position[1] + new_position[1]] == BOX:
        new_map[current_node.position[0] + new_position[0]][current_node.position[1] + new_position[1]] = EMPTY
        new_box_position = (
            current_node.position[0] + 2 * new_position[0], current_node.position[1] + 2 * new_position[1])
        new_map[new_box_position[0]][new_box_position[1]] = BOX
    return new_map


def generate_children(current_node):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure walkable terrain
        if current_node.state[node_position[0]][node_position[1]] == WALL:
            continue
        if current_node.state[node_position[0]][node_position[1]] == BOX:
            new_box_position = (node_position[0] + new_position[0], node_position[1] + new_position[1])
            if IS_SOLID(current_node.state[new_box_position[0]][new_box_position[1]]):
                continue

        new_state = generate_new_state(current_node, new_position)

        # Create new node
        new_node = Node(current_node, node_position, new_state)

        # Append
        children.append(new_node)

    return children


def create_path(initial_node, current_node):
    path = [current_node.position]
    while current_node.position != initial_node.position:
        current_node = current_node.parent
        path.append(current_node.position)
    return path[::-1]  # Doy vuelta asi arranca por el nodo inicial.
