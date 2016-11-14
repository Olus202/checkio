import string


def checkio(words):
    elements = words.split(" ")
    
    if len(elements) < 3:
        return False

    for ind, e in enumerate(elements):
        try:
            if e[-1] in string.digits:
                elements[ind] = "0"
        except:
            if e in string.digits:
                elements[ind] = "0"
    
    n = 0
    for i in elements:
        if i != "0":
            n += 1
        else:
            n = 0
        if n == 3:
            return True
    
    return False
