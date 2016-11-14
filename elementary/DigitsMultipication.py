# https://checkio.org/mission/digits-multiplication/


def checkio(number):
    r = 1
    for n in str(number):
        if n != "0":
            r *= int(n)
    return r
