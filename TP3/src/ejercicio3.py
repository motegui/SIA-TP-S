from Neuron import *
from Layer import *
from TP3.src.kfold import kfold_cross_validation_multilayer
from TP3.src.metrics import test_network, numbers_test, even_test
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

    print('Error is ', error)

    print("/////////////////////////////////////")
    print(network.forward_propagation([1, -1]))
    print("/////////////////////////////////////")
    print(network.forward_propagation([-1, -1]))
    print(network.forward_propagation([-1, 1]))
    print(network.forward_propagation([1, 1]))

    print('----------------------------------------------------')
    # excercise 3.b
    #without extra data
    csv_file = '/Users/pazaramburu/Desktop/SIA-TP-S/TP3/data/TP3-ej3-digitos.txt'

    clean_numbers = transform_csv_to_list(csv_file)
    expected_output = get_expected_even()

    layer1 = layer_n_neurons(3, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(1, hyp_tan_theta, hyp_tan_prime_theta)
    network = Network([layer1, layer2])
    input_data = get_clean_matrix(clean_numbers)
    kfold_cross_validation_multilayer([input_data, expected_output],network,35, 4, even_test)


    noise_data = create_numbers_with_noise_even(clean_numbers, 5)
    noise_data_input = [list(arr) for arr in noise_data[0]]


    #train all the numbers and test numbers with noise
    error_train = multilayer_perceptron(input_data, expected_output, compute_error_multilayer, 200000, 0.1, network)
    print(test_network(network, [noise_data_input, noise_data[1]], even_test))

    #train the numbers with noise and test the real numbers
    error_train = multilayer_perceptron(noise_data_input, noise_data[1], compute_error_multilayer, 200000, 0.2,
                                        network)
    print(test_network(network, [input_data, expected_output], even_test))

    #shuffle the noise and real numbers and divide in train and test
    x_shuffle, y_shuffle = shuffle_arrays(input_data + noise_data_input, expected_output + noise_data[1])
    kfold_cross_validation_multilayer([x_shuffle, y_shuffle], network, 35, 4, even_test)

    print('----------------------------------------------------')

    # excercise 3.c

    clean_numbers = transform_csv_to_list("/Users/pazaramburu/Desktop/SIA-TP-S/TP3/data/TP3-ej3-digitos.txt")
    expected_output = get_expected_digits()

    # training
    layer1 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)

    network = Network([layer1, layer2])
    input_data = get_clean_matrix(clean_numbers)
    noise_data = create_numbers_with_noise(clean_numbers, 10)
    noise_data_input = [list(arr) for arr in noise_data[0]]
    x_shuffled, y_shuffled = shuffle_arrays(input_data + noise_data_input, expected_output + noise_data[1])

    kfold_cross_validation_multilayer([x_shuffled, y_shuffled], network, 35, 5, numbers_test)



if __name__ == '__main__':
    main()
