from utils import *


class Layer:
    def __init__(self, neurons=None):
        self.neurons = neurons
        self.neuron_len = len(neurons)

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs([1] + inputs)
            out.append(neuron.compute_output())
        return out

    def updated_forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs([1] + inputs)
            out.append(neuron.compute_updated_output())
        return out

    def populate_weights(self, input_count=None):
        for neuron in self.neurons:
            weights = random_initialize_weight(input_count-1)
            neuron.set_weights([0] + weights)  # aca hay que agregar el bias

    def get_weights(self):
        return [neuron.weights for neuron in self.neurons]

    def compute_deltas(self, prev_deltas, connected_weights):  # connected_weights es un vector de vectores y para neurona_i uso connected_i
        deltas = []
        for i in range(len(self.neurons)):
            self.neurons[i].compute_delta(prev_deltas,
                                          np.array(connected_weights)[:, i + 1])  # TODO ESTAMOS SACANDO EL VIAS
            deltas.append(self.neurons[i].delta)
        return deltas

    def update_neuron_weights(self):
        for neuron in self.neurons:
            neuron.update_weights()

    def __str__(self):
        return '\n'.join([str(neuron) for neuron in self.neurons])
