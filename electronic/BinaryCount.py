def checkio(number):
    binNumber = bin(number)
    units = binNumber.count("1")
    return units
