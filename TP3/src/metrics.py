import numpy as np


def accuracy(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + fp + fn)


def presicion(tp, fp):
    if tp == 0:
        return 0
    return tp / (tp + fp)


def recall(tp, fn):
    if tp == 0:
        return 0
    return tp / (tp + fn)


def f1_score(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * precision * recall / (precision + recall)


def numbers_test(network, data):
    input_data = data[0]
    real_numbers = data[2]
    confusion_matrix = np.zeros((10, 10))

    for input, expected_number in zip(input_data, real_numbers):
        prediction = network.forward_propagation(input)
        predicted_number = np.argmax(prediction)
        confusion_matrix[expected_number][predicted_number] += 1

    return confusion_matrix


def even_test(network, data): # [0] recibe los input data, y en el valor [1] un array de [1 y -1]
    input_data = data[0]
    output_even_odd = data[1]
    confusion_matrix = np.zeros((2, 2))

    for input, expected_number in zip(input_data, output_even_odd):
        prediction = network.forward_propagation(input)
        # mayor a 0 par
        # 0 clase par
        # 1 clase impar
        predicted_number = 0 if prediction[0] > 0 else 1
        expected_number = 0 if expected_number[0] > 0 else 1
        confusion_matrix[expected_number][predicted_number] += 1

    return confusion_matrix


def test_network(network, data, eval):
    confusion_matrix = eval(network, data)
    class_metrics = []
    metrics_array = []
    for i in range(confusion_matrix.shape[0]):
        tp = confusion_matrix[i][i]
        fn = sum(confusion_matrix[i]) - tp
        fp = np.sum(confusion_matrix[:, i]) - tp
        tn = np.sum(confusion_matrix) - (tp + fn + fp)

        ac = accuracy(tp, tn, fp, fn)
        pr = presicion(tp,fp)
        rec = recall(tp,fn)
        f1 = f1_score(presicion(tp,fp), recall(tp,fn))
        class_metrics.append({
            "clase": i,
            "accuracy": ac,
            "precision": pr,
            "recall": rec,
            "f1": f1
        })
        metrics_array.append([i, ac, pr, rec, f1])
    return class_metrics, metrics_array

