def normalize(data, new_min, new_max):
    data_min = data.min()
    data_max = data.max()
    return [(new_max - new_min) * (x - data_min) / (data_max - data_min) + new_min for x in data]


def denormalize(data, new_min, new_max):
    data_min = min(data)
    data_max = max(data)
    return [(x - data_min) * (new_max - new_min) / (data_max - data_min) + new_min for x in data]
