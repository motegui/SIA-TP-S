class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs(inputs)
            out.append(neuron.compute_excitement())
        return out