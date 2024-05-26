class Neuron:
    def __init__(self, weights, x, y):
        self.weights = weights
        self.x = x
        self.y = y

    def update_weights(self, x, learning_rate):
        self.weights += learning_rate * (x-self.weights)

    def get_weights(self):
        weights = [x.astype(float) for x in self.weights]
        return weights
