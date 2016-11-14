data_list = [2, 3, 1]


def checkio(data):
    data.sort()
    if len(data) % 2 != 0:
        return data[int((len(data)) / 2)]
    else:
        return (data[int(len(data) / 2)] + data[(int(len(data) / 2)) - 1]) / 2

checkio(data_list)
