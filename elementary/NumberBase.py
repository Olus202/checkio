# https://checkio.org/mission/number-radix/


def checkio(str_number, radix):
    try:
        cunvertedNum = int(str_number, radix)
        return cunvertedNum
    except:
        return -1
