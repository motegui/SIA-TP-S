from TP1.utils.state import State


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.read().split('\n')
    #search for the max length in lines
    length = max(len(line) for line in lines)
    matrix = []
    for line in lines:
        padded_line = line.ljust(length, '#')
        row = list(padded_line)
        matrix.append(row)

    return matrix


def process_map(map):
    matrix_1 = []
    box_positions = []
    goal_positions = []
    start_position = None

    for i in range(len(map)):
        row_1 = []
        for j in range(len(map[i])):
            if map[i][j] == '@':
                start_position = (i, j)
                row_1.append(ord(' '))
            elif map[i][j] == '$':
                row_1.append(ord(map[i][j]))
                box_positions.append((i, j))
            elif map[i][j] == '.':
                row_1.append(ord(' '))
                goal_positions.append((i, j))
            elif map[i][j] == '*':
                row_1.append(ord('$'))
            else:
                row_1.append(ord(map[i][j]))

        matrix_1.append(row_1)
    state = State(matrix_1, goal_positions, box_positions)
    return state, start_position

