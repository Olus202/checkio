word = "so sad das-li"


def palindromic(palin):

    if palin == palin[::-1]:
        return True

    return False


def checkio(text):
    longestpalin = ""
    for m in range(len(text)):
        for n in range(len(text) + 1):
            palin = text[m:n]
            if palindromic(palin):
                if len(palin) > len(longestpalin):
                    longestpalin = palin
            print(palin, longestpalin)

    return longestpalin


print(checkio(word))
