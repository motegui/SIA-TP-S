import random


def random_initializer(input_data) -> list:
    return [random.uniform(0, 1) for _ in input_data[0] - 1]


def input_initializer(input_data) -> list:
    u = random.randint(0, len(input_data) - 1)
    return input_data.pop(u)[1:]
