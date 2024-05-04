from Neuron import *
from Layer import *
from theta_functions import *
from Network import *
from perceptron import multilayer_perceptron


def main():
    #excercise 3.a
    # layer1 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    # layer2 = layer_n_neurons(1, hyp_tan_theta, hyp_tan_prime_theta)
    # network = Network([layer1, layer2])
    #
    # network.initialize(input_count=2)
    #
    # input_data = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    # output_data = [[-1], [1], [1], [-1]]
    # error = multilayer_perceptron(input_data, output_data, compute_error_multilayer, 90000, 0.1, network)
    #
    # print(error)
    #
    # print(network.forward_propagation([1, -1]))
    # print(network.forward_propagation([-1, -1]))
    # print(network.forward_propagation([-1, 1]))
    # print(network.forward_propagation([1, 1]))
    #
    # print(network)
    print('----------------------------------------------------')
    #excercise 3.c

    csv_file = '/Users/pazaramburu/Desktop/SIA-TP-S/TP3/data/TP3-ej3-digitos.txt'
    clean_numbers = transform_csv_to_list(csv_file)
    expected_output = get_expected_output()

    #training
    layer1 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    layer3 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    network = Network([layer1,  layer3])
    network.initialize(input_count=35)
    input_data = get_clean_matrix(clean_numbers)
    error = multilayer_perceptron(input_data, expected_output, compute_error_multilayer, 30000, 0.1, network)

    # print(error)


    #testing
    noise_data = create_numbers_with_noise(clean_numbers, 3)
    print(network.forward_propagation(noise_data[0][0].tolist()))
    print(network.forward_propagation(noise_data[0][1*3].tolist()))
    print(network.forward_propagation(noise_data[0][2*3].tolist()))
    print(network.forward_propagation(noise_data[0][3*3].tolist()))
    print(network.forward_propagation(noise_data[0][4*3].tolist()))
    print(network.forward_propagation(noise_data[0][5*3].tolist()))
    print(network.forward_propagation(noise_data[0][6*3].tolist()))
    print(network.forward_propagation(noise_data[0][7*3].tolist()))
    print(network.forward_propagation(noise_data[0][8*3].tolist()))
    print(network.forward_propagation(noise_data[0][9*3].tolist()))

    print(expected_output[0])







if __name__ == '__main__':
    main()

