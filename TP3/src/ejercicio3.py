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

    print('error is ', error)

    print('weights are',network.get_weights())
    print("/////////////////////////////////////")
    print(network.forward_propagation([1, -1]))
    print("/////////////////////////////////////")
    print(network.forward_propagation([-1, -1]))
    print(network.forward_propagation([-1, 1]))
    print(network.forward_propagation([1, 1]))

    print(network)
    print('----------------------------------------------------')
    # excercise 3.b
    #without extra data
    # csv_file = '/Users/pazaramburu/Desktop/SIA-TP-S/TP3/data/TP3-ej3-digitos.txt'
    #
    # clean_numbers = transform_csv_to_list(csv_file)
    # expected_output = get_expected_even()
    #
    # layer1 = layer_n_neurons(3, hyp_tan_theta, hyp_tan_prime_theta)
    # layer2 = layer_n_neurons(1, hyp_tan_theta, hyp_tan_prime_theta)
    # network = Network([layer1, layer2])
    # input_data = get_clean_matrix(clean_numbers)
    # # kfold_cross_validation_multilayer([input_data, expected_output],network,35, 4)
    # network.initialize(input_count=35)
    #
    # split_index = int(0.6 * len(input_data))
    # X_train, y_train = input_data[:split_index], expected_output[:split_index]
    # X_test, y_test = input_data[split_index:], expected_output[split_index:]
    #
    # error_train = multilayer_perceptron(X_train, y_train, compute_error_multilayer, 200000, 0.01, network)
    # print("error train:", error_train)
    # print(network.forward_propagation(X_train[2]))
    # for i in range(len(X_test)):
    #     result = "par" if network.forward_propagation(X_test[i])[0] > 0 else "impar"
    #     exp = "par" if y_test[i][0] == 1 else "impar"
    #     print("result:", result, "expected:", exp)

    # noise_data = create_numbers_with_noise_even(clean_numbers, 5)
    # noise_data_input = [list(arr) for arr in noise_data[0]]


    #train all the numbers and test numbers with noise
    # error_train = multilayer_perceptron(input_data, expected_output, compute_error_multilayer, 200000, 0.1, network)
    # print("error train:", error_train)
    # print(test_network(network, [noise_data_input, noise_data[1]], even_test))

    #train the numbers with noise and test the real numbers
    # error_train = multilayer_perceptron(noise_data_input, noise_data[1], compute_error_multilayer, 200000, 0.2,
    #                                     network)
    # print("error train:", error_train)
    # print(test_network(network, [input_data, expected_output], even_test))
    # for i in range(len(input_data)):
    #     result = "par" if network.forward_propagation(input_data[i])[0] > 0 else "impar"
    #     exp = "par" if expected_output[i][0] == 1 else "impar"
    #     print("result:", result, "expected:", exp)

    #shuffle the noise and real numbers and divide in train and test
    #agregar un 0 mas a step
    # x_shuffle, y_shuffle = shuffle_arrays(input_data + noise_data_input, expected_output + noise_data[1])
    # kfold_cross_validation_multilayer([x_shuffle, y_shuffle], network, 35, 4)
    # split_index = int(0.8 * len(x_shuffle))
    #
    # X_train, y_train = x_shuffle[:split_index], y_shuffle[:split_index]
    # X_test, y_test = x_shuffle[split_index:], y_shuffle[split_index:]
    # error_train = multilayer_perceptron(X_train, y_train, compute_error_multilayer, 200000, 0.01,
    #                                     network)
    # print("error train:", error_train)
    # for i in range(len(X_test)):
    #     result = "par" if network.forward_propagation(X_test[i])[0] > 0 else "impar"
    #     exp = "par" if y_test[i][0] == 1 else "impar"
    #     print("result:", result, "expected:", exp)


    # excercise 3.c

    # clean_numbers = transform_csv_to_list("/Users/lucho/Desktop/Repos/SIA-TP-S/TP3/data/TP3-ej3-digitos.txt")
    # expected_output = get_expected_digits()
    #
    # # training
    # layer0 = layer_n_neurons(100, hyp_tan_theta, hyp_tan_prime_theta)
    # layer1 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    # layer2 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    # layer5 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    # layer6 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    # layer3 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    #
    # network = Network([layer5, layer3])
    # input_data = get_clean_matrix(clean_numbers)
    # noise_data = create_numbers_with_noise(clean_numbers, 20)
    # noise_data_input = [list(arr) for arr in noise_data[0]]
    # x_shuffled, y_shuffled = shuffle_arrays(input_data + noise_data_input, expected_output + noise_data[1])
    # # print(x_shuffled)
    # # print(y_shuffled)
    # # kfold_cross_validation_multilayer([x_shuffled, y_shuffled], network, 35, 5)
    # network.initialize(input_count=35)
    # error = multilayer_perceptron(input_data, expected_output, compute_error_multilayer, 100000, 0.5, network)
    # print(network.get_weights())
    # print(error)
    # metrics, metrix_mat = test_network(network, noise_data, numbers_test)
    # print(metrix_mat)

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
