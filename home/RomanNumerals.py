# https://checkio.org/mission/roman-numerals/

number = 99

def checkio(number):
    romannumbers = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
    rest = number
    romanstring = ""
    for romannumber in romannumbers:
        m = rest // romannumbers[romannumbers.index(romannumber)][1]
        if str(rest)[0] == "9":
            if len(str(rest)) == 3:
                romanstring = romanstring + "CM"
            if len(str(rest)) == 2:
                romanstring = romanstring + "XC"
            if len(str(rest)) == 1:
                romanstring = romanstring + "IX"
        elif str(rest)[0] == "4":
            romanstring = romanstring
        else:
            romanstring = romanstring + m * romannumbers[romannumbers.index(romannumber)][0]
        rest = rest % romannumbers[romannumbers.index(romannumber)][1]

    return romanstring

print(checkio(number))