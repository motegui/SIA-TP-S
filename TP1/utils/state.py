class State:
    def __init__(self, current_map=None, goals=None, boxes=None):
        self.current_map = current_map
        self.goals = goals
        self.boxes = boxes

    def is_final(self):
        used_goals = []
        for box in self.boxes:
            for goal in self.goals:
                if goal not in used_goals:
                    if box == goal:
                        used_goals.append(goal)
        return len(used_goals) == len(self.goals)

    def __eq__(self, other):
        return (all([a == b for a, b in zip(self.current_map, other.current_map)]) and self.goals == other.goals and
                self.boxes == other.boxes)
