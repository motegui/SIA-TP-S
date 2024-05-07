from Neuron import *
from Layer import *
from TP3.src.kfold import kfold_cross_validation_multilayer
from theta_functions import *
from Network import *
from perceptron import *


def main():
    # excercise 3.a
    layer1 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(1, hyp_tan_theta, hyp_tan_prime_theta)
    network = Network([layer1, layer2])

    network.initialize(input_count=2)

    input_data = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    output_data = [[-1], [1], [1], [-1]]
    error = multilayer_perceptron(input_data, output_data, compute_error_multilayer, 100000, 0.1, network)

    print('error is ', error)

    print('weights are',network.get_weights())
    print("/////////////////////////////////////")
    print(network.forward_propagation([1, -1]))
    print("/////////////////////////////////////")
    print(network.forward_propagation([-1, -1]))
    print(network.forward_propagation([-1, 1]))
    print(network.forward_propagation([1, 1]))

    # print(network)
    print('----------------------------------------------------')
    # excercise 3.c

    # clean_numbers = transform_csv_to_list(csv_file)
    expected_output = get_expected_digits()

    # training
    # layer0 = layer_n_neurons(100, hyp_tan_theta, hyp_tan_prime_theta)
    # layer1 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    # layer2 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    # layer5 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    # layer6 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    layer3 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)

    # network = Network([layer5, layer3])
    # input_data = get_clean_matrix(clean_numbers)
    # noise_data = create_numbers_with_noise(clean_numbers, 20)
    # noise_data_input = [list(arr) for arr in noise_data[0]]
    # x_shuffled, y_shuffled = shuffle_arrays(input_data + noise_data_input, expected_output + noise_data[1])
    # print(x_shuffled)
    # print(y_shuffled)
    # kfold_cross_validation_multilayer([x_shuffled, y_shuffled], network, 35, 5)
    # network.initialize(input_count=35)
    # error = multilayer_perceptron(input_data, expected_output, compute_error_multilayer, 200000, 0.33, network)
    # print(network.get_weights())
    # print(error)
    # test_network(network, [noise_data_input, noise_data[1]])

    # network.initialize(35)

    # print(noise_data[0][2].tolist())
    #
    # print(network.forward_propagation(noise_data[0][8].tolist()))

    # testing
    # print(network.forward_propagation(noise_data[0][0].tolist()))
    # print(network.forward_propagation(noise_data[0][1*3].tolist()))
    # print(network.forward_propagation(noise_data[0][2*3].tolist()))
    # print(network.forward_propagation(noise_data[0][3*3].tolist()))
    # print(network.forward_propagation(noise_data[0][4*3].tolist()))
    # print(network.forward_propagation(noise_data[0][5*3].tolist()))
    # print(network.forward_propagation(noise_data[0][6*3].tolist()))
    # print(network.forward_propagation(noise_data[0][7*3].tolist()))
    # print(network.forward_propagation(noise_data[0][8*3].tolist()))
    # print(network.forward_propagation(noise_data[0][9*3].tolist()))

    # print(expected_output[0])


if __name__ == '__main__':
    main()
