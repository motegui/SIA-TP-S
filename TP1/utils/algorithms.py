import collections
import time
from copy import deepcopy
from heuristics import *
from algorithms_utils import *
from node import Node
from process_map import *


def bfs(initial_map, start_position, goal_map, generate_children):
    expanded_nodes = 0
    initial_node = Node(None, start_position, initial_map)
    end_node = Node(None, None, goal_map)
    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.popleft()  # Remove and return the leftmost element.
        if current_node.state_equals(end_node):
            return create_response(current_node, expanded_nodes, len(opened_list))

        # Children are created dynamically
        for child in generate_children(current_node, goal_map):
            expanded_nodes += 1
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def dfs(initial_map, start_position, goal_map, generate_children):
    expanded_nodes = 0
    initial_node = Node(None, start_position, initial_map)
    end_node = Node(None, None, goal_map)
    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.pop()  # Remove and return the rightmost element.
        if current_node.state_equals(end_node):
            return create_response(current_node, expanded_nodes, len(opened_list))

        expanded_nodes += 1
        # Children are created dynamically
        for child in generate_children(current_node, goal_map):
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def local_greedy(initial_map, start_position, goal_map, generate_children, heuristic):
    expanded_nodes = 0
    closed_list = []

    initial_node = Node(None, start_position, initial_map)
    initial_node.h = heuristic(initial_map, goal_map, start_position)
    initial_node.g = 0
    initial_node.f = initial_node.h

    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()

        if current_node.state_equals(end_node):
            return create_response(current_node, expanded_nodes, len(opened_list))

        ordered_children = sorted(generate_children(current_node, goal_map), key=lambda x: x.h, reverse=True)
        expanded_nodes += 1
        # Children are created dynamically
        for child in ordered_children:
            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child
            child.h = heuristic(child.state, goal_map, child.position)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def global_greedy(initial_map, start_position, goal_map, generate_children, heuristic):
    expanded_nodes = 0
    closed_list = []

    initial_node = Node(None, start_position, initial_map)
    initial_node.h = heuristic(initial_map, goal_map, start_position)
    initial_node.g = 0
    initial_node.f = initial_node.h

    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()

        if current_node.state_equals(end_node):
            return create_response(current_node, expanded_nodes, len(opened_list))

        children = generate_children(current_node, goal_map)
        expanded_nodes += 1
        # Children are created dynamically
        for child in children:
            child.g = current_node.g + 1
            child.h = heuristic(child.state, goal_map, child.position)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)

        opened_list = collections.deque(sorted(opened_list, key=lambda x: x.h, reverse=True))


def astar(initial_map, start_position, goal_map, generate_children, heuristic):
    expanded_nodes = 0
    initial_node = Node(None, start_position, initial_map)
    initial_node.h = heuristic(initial_map, goal_map, start_position)
    initial_node.g = 0
    initial_node.f = initial_node.h

    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = [initial_node]
    closed_list = []

    while opened_list:

        current_node = opened_list[0]
        current_index = 0
        for (i, node) in enumerate(opened_list):
            if node.f == current_node.f and node.h < current_node.h:
                current_node = node
                current_index = i
            elif node.f < current_node.f:
                current_node = node
                current_index = i

        opened_list.pop(current_index)
        closed_list.append(current_node)
        if current_node.state_equals(end_node):
            return create_response(current_node, expanded_nodes, len(opened_list))

        # Children are created dynamically
        children = generate_children(current_node, goal_map)
        expanded_nodes += 1

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = heuristic(child.state, goal_map, child.position)
            child.f = child.g + child.h

            is_open = False
            for openNode in opened_list:
                if child == openNode and child.g > openNode.g:
                    is_open = True
            if is_open:
                continue
            opened_list.append(child)


def create_response(current_node, expanded_nodes, opened_list_size):
    path = [current_node.position]
    while current_node.parent is not None:
        current_node = current_node.parent
        path.append(current_node.position)
    path = path[::-1]
    if path is None:
        return ["failure", None, expanded_nodes, opened_list_size, None]
    return ["Success", len(path), expanded_nodes, opened_list_size, path]


def main():
    responses = []
    for i in range(4, 7):
        start_time = time.time()
        m1, m2, start = process_map(read_file("../Levels/level" + str(i) + ".txt"))
        print("entrando al level: ", i)
        print(m1, m2, start)
        response = global_greedy(m1, start, m2, generate_children_sokoban, manhattan_heuristic)
        response.append((time.time() - start_time))
        responses.append(response)
    return responses


# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]

if __name__ == '__main__':
    print(main())
