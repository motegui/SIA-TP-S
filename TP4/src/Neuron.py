class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def update_weights(self, x, learning_rate):
        self.weights += learning_rate * (x-self.weights)

