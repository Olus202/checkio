# https://checkio.org/mission/pawn-brotherhood/

pawns = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}


def defense(s):
    global defen
    files = "abcdefgh"
    let = s[0]
    dig = s[1]
    if let == "a":
        d = int(dig) - 1
        defen = ["b" + str(d), ""]
    elif let in "bcdefg":
        l1 = files[files.index(let) - 1]
        l2 = files[files.index(let) + 1]
        d = int(dig) - 1
        defen = [l1 + str(d), l2 + str(d)]
    elif let == "h":
        d = int(dig) - 1
        defen = ["g" + str(d), ""]
    return defen


def safe_pawns(pawns):
    safe = 0
    for i in pawns:
        df = defense(i)
        if df[0] in pawns or df[1] in pawns:
            safe += 1
    return safe

print(safe_pawns(pawns))