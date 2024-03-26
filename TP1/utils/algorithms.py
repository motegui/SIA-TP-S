import collections
import heapq
import time
from copy import deepcopy
from heuristics import *
from algorithms_utils import *
from node import Node
from process_map import *


def bfs(state, start_position, generate_children):
    expanded_nodes = 0
    initial_node = Node(None, start_position, state)

    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.popleft()  # Remove and return the leftmost element.
        if current_node.state.is_final():
            return create_response(current_node, expanded_nodes, len(opened_list))

        # Children are created dynamically
        for child in generate_children(current_node):
            expanded_nodes += 1
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def dfs(state, start_position, generate_children):
    expanded_nodes = 0
    initial_node = Node(None, start_position, state)

    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.pop()  # Remove and return the rightmost element.
        if current_node.state.is_final():
            return create_response(current_node, expanded_nodes, len(opened_list))

        expanded_nodes += 1
        # Children are created dynamically
        for child in generate_children(current_node):
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def local_greedy(state, start_position, generate_children, heuristic):
    expanded_nodes = 0
    closed_list = []

    initial_node = Node(None, start_position, state)
    initial_node.h = heuristic(initial_node)
    initial_node.g = 0
    initial_node.f = initial_node.h

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()
        if current_node.state.is_final():
            return create_response(current_node, expanded_nodes, len(opened_list))

        ordered_children = sorted(generate_children(current_node), key=lambda x: heuristic(x), reverse=True)
        expanded_nodes += 1
        # Children are created dynamically
        for child in ordered_children:
            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child
            child.h = heuristic(child)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def global_greedy(state, start_position, generate_children, heuristic):
    expanded_nodes = 0
    closed_list = []

    initial_node = Node(None, start_position, state)
    initial_node.h = heuristic(initial_node)
    initial_node.g = 0
    initial_node.f = initial_node.h

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()

        if current_node.state.is_final():
            return create_response(current_node, expanded_nodes, len(opened_list))

        children = generate_children(current_node)
        expanded_nodes += 1
        # Children are created dynamically
        for child in children:
            child.g = current_node.g + 1
            child.h = heuristic(child)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)

        opened_list = collections.deque(sorted(opened_list, key=lambda x: x.h, reverse=True))


def astar(state, start_position, generate_children, heuristic):
    expanded_nodes = 0

    initial_node = Node(None, start_position, state)
    initial_node.h = heuristic(initial_node)
    initial_node.g = 0
    initial_node.f = initial_node.h

    opened_list = [initial_node]
    closed_list = []

    while opened_list:

        current_node = opened_list.pop()

        if current_node.state.is_final():
            return create_response(current_node, expanded_nodes, len(opened_list))

        # Children are created dynamically
        children = generate_children(current_node)
        expanded_nodes += 1

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = heuristic(child)
            child.f = child.g + child.h

            is_open = False
            is_contained = False
            for openNode in opened_list:
                if child == openNode:
                    is_contained = True
                    if child.g > openNode.g:
                        is_open = True
                        continue
            if is_open:
                continue
            if is_contained:
                opened_list.remove(child)
            opened_list.append(child)
            closed_list.append(current_node)

        opened_list = collections.deque(sorted(opened_list, key=lambda x: (x.f, x.h), reverse=True))



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
    for i in range(6, 7):
        start_time = time.time()
        state, end_state, start = process_map(read_file("../Levels/level" + str(i) + ".txt"))
        print("entrando al level: ", i)
        # print(state.current_map, start)
        response = astar(state, start, generate_children_sokoban, manhattan_heuristic)
        responses.append((time.time() - start_time))
        responses.append(response)
    return responses



if __name__ == '__main__':
    print(main())
