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

    def state_equals(self, other):
        return all([a == b for a, b in zip(self.state, other.state)])