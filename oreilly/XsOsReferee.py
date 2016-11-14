lista = ["OOX", "XXO", "OXX"]


def checkio(lista):
    if lista[0][0] == lista[1][1] and lista[0][0] == lista[2][2]:
        print(lista[0][0])
    elif lista[0][2] == lista[1][1] and lista[0][2] == lista[2][0]:
        print(lista[0][0])
    elif lista[0][0] == lista[1][0] and lista[0][0] == lista[2][0]:
        print(lista[0][0])
    elif lista[0][1] == lista[1][1] and lista[0][1] == lista[2][1]:
        print(lista[0][1])
    elif lista[0][2] == lista[1][2] and lista[0][2] == lista[2][2]:
        print(lista[0][2])
    elif lista[0][0] == lista[0][1] and lista[0][0] == lista[0][2]:
        print(lista[0][0])
    elif lista[1][0] == lista[1][1] and lista[1][0] == lista[1][2]:
        print(lista[1][0])
    elif lista[2][0] == lista[2][1] and lista[2][0] == lista[2][2]:
        print(lista[2][0])
    else:
        print("D")

checkio(lista)
