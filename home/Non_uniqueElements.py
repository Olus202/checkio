# https://checkio.org/mission/non-unique-elements/

data = [1, 2, 3, 4, 5]
data2 = []

for i in data:
    print(data.count(i))
    s = int(data.count(i))
    if s != 1:
        data2.append(i)
data = data2

print(data)
