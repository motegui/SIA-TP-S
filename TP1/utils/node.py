class Node:
    def __init__(self, parent=None, position=None, state=None):
        self.parent = parent
        self.position = position
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state and self.position == other.position

    def __hash__(self):
        return hash((self.parent, self.position, self.state))

    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f

    def state_equals(self, other):
        return all([a == b for a, b in zip(self.state, other.state)])

