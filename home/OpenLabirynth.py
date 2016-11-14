def check_X(p):
    if d == "S":
        check_E(result, p, r, c, d)
    elif d == "E":
        check_N(result, p, r, c, d)
    elif d == "N":
        check_W(result, p, r, c, d)
    else:
        check_S(result, p, r, c, d)


def check_S(result, p, r, c, d):

    if p[r + 1][c] == 0:
        r = r + 1
        d = "S"
        result += d
    elif p[r + 1][c] == "X":
        check_X(result, p, r, c, d)
    else:
        check_E(result, p, r, c, d)

    print("S", result, p, r, c, d)
    return result, p, r, c, d


def check_E(result, p, r, c, d):
    if p[r][c + 1] == 0:
        c = c + 1
        d = "E"
        result += d
    elif p[r][c + 1] == "X":
        check_X(result, p, r, c, d)
    else:
        check_N(result, p, r, c, d)

    return result, p, r, c, d


def check_N(result, p, r, c, d):
    if p[r - 1][c] == 0:
        r = r - 1
        d = "N"
        result += d
    elif p[r - 1][c] == "X":
        check_X(result, p, r, c, d)
    else:
        check_W(result, p, r, c, d)

    return result, p, r, c, d


def check_W(result, p, r, c, d):
    if p[r][c - 1] == 0:
        c = c - 1
        d = "E"
    elif p[r][c - 1] == "X":
        check_X(result, p, r, c, d)
    else:
        check_S(result, p, r, c, d)

    return result, p, r, c, d


def checkio(maze_map):
    r = 1
    c = 1
    d = "S"
    p = maze_map
    result = "a"
    check_S(result, p, r, c, d)

    return result

print(checkio([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        ))
