# https://checkio.org/mission/index-power/


def index_power(array, n):
    if n > len(array) - 1:
        result = -1
    else:
        result = array[n]**n
    return result
