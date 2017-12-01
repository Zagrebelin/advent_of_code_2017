def calc(data):
    if type(data) is str:
        data = list(map(int, data))
    d2 = data[1:]
    s = sum(a for a, b in zip(data, d2) if a == b)
    if data[0] == data[-1]:
        s += data[0]
    return s


assert calc('1122') == 3
assert calc('1111') == 4
assert calc('1234') == 0
assert calc('91212129') == 9

data = open('data/day_01').read()
print(calc(data))
