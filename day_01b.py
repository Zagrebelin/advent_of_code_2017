import itertools


def calc(data):
    if type(data) is str:
        data = list(map(int, data))
    l = int(len(data) / 2)
    d2 = itertools.chain(data[l:], data[:l])
    s = sum(a for a, b in zip(data, d2) if a == b)
    return s


assert calc('1212') == 6
assert calc('1221') == 0
assert calc('123425') == 4
assert calc('123123') == 12
assert calc('12131415') == 4

data = open('data/day_01').read()
print(calc(data))
