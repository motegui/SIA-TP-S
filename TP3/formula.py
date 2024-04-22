from utils import *


def __feed_perceptron():
    # AND
    input_data = [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    expected_output = [-1, -1, 1, -1]
    t = staggered_perceptron(input_data, expected_output, random_initialize_weight, compute_error, 1000, 0.1)
    # XOR 1 1
    input_data2 = [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    expected_output2 = [1, -1, -1, 1]
    t2 = staggered_perceptron(input_data2, expected_output2, random_initialize_weight, compute_error, 30, 0.1)
    print(t2[1])
    return [t[0], t2[0]]


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None


def __build_tree(formula):
    formula.strip()
    if formula.startswith('('):
        formula = formula[1:-1]

    if formula in ("1", "-1"):
        return Node(formula)

    tokens = formula.split()

    idx = __find_central_operator(tokens)

    root = Node(tokens[idx])

    root.left = __build_tree(" ".join(tokens[:idx]))
    root.right = __build_tree(" ".join(tokens[idx + 1:]))
    return root


def __find_central_operator(tokens):
    parenthesis = 0
    for idx, token in enumerate(tokens):
        if token == "(":
            parenthesis += 1
        elif token == ")":
            parenthesis -= 1
        elif token in ("and", "xor") and parenthesis == 0:
            return idx
    return -1


def __evaluate_formula(tree, w_and, w_xor):
    if tree.valor in ('1', '-1'):
        return int(tree.valor)
    if tree.valor in ("and", "xor"):
        x1 = __evaluate_formula(tree.left, w_and, w_xor)
        x2 = __evaluate_formula(tree.right, w_and, w_xor)
        if tree.valor == "and":
            return 1 if sum(np.multiply([1, x1, x2], w_and)) >= 0 else -1
        else:
            return 1 if sum(np.multiply([1, x1, x2], w_xor)) >= 0 else -1


def evaluate_formula(formula):
    [w_and, w_xor] = __feed_perceptron()
    print(w_xor)

    tree = __build_tree(formula)
    val = __evaluate_formula(tree, w_and, w_xor)
    return True if val >= 0 else False
