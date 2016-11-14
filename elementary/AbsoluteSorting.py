def checkio(numbers_array):
    abs_dict= {abs(k): k for k in numbers_array}
    print(abs_dict)
    new_list = [abs(x) for x in numbers_array]
    print(new_list)
    new_list.sort()
    print(new_list)
    for i in new_list:
        index = new_list.index(i)
        new_list[index] = abs_dict[i]
    return new_list


checkio((-20, -5, 10, 15))