from aocframe import AoCFramework


def show(matrix):
    minx = int(min(matrix, key=lambda x: x.real).real)
    miny = int(min(matrix, key=lambda x: x.imag).imag)
    maxx = int(max(matrix, key=lambda x: x.real).real + 1)
    maxy = int(max(matrix, key=lambda x: x.imag).imag + 1)

    for x in range(minx, maxx):
        for y in range(miny, maxy):
            value = matrix.get(complex(x, y), '?')
            print('[%s:%s]%s' % (x, y, value), end=' ')
        print('')


class Part1(AoCFramework):
    atest_cases = [('1024', 31), ('23', 2), ('12', 3), ('1', 0), ('2', 1), ('3', 2), ('4', 1), ('5', 2), ('6', 1),
                   ('7', 2), ('8', 1), ('9', 2), ('10', 3)]
    known_result = 552

    def go(self, data):
        stop = int(data)
        matrix = {}
        for current, pos in enumerate(self.next_cell_coord(matrix), start=1):
            matrix[pos] = current
            if current == stop:
                return int(abs(pos.imag) + abs(pos.real))

    def next_cell_coord(self, matrix, start=complex(0, 0)):
        looks = [complex(0, -1), complex(-1, 0), complex(0, 1), complex(1, 0)]
        steps = [complex(1, 0), complex(0, -1), complex(-1, 0), complex(0, 1)]
        look_idx = 0
        step_idx = 0
        pos = start
        while True:
            yield pos
            pos = pos + steps[step_idx]
            if pos + looks[look_idx] not in matrix:
                look_idx = (look_idx + 1) % len(looks)
                step_idx = (step_idx + 1) % len(steps)


class Part2(Part1):
    known_result = 330785

    def go(self, data):
        stop = int(data)
        matrix = {complex(0, 0): 1}
        for pos in self.next_cell_coord(matrix):
            current = sum(self.neigbours_values(matrix, pos))
            matrix[pos] = current
            if current> stop:
                return current

    def neigbours_values(self, matrix, pos, default=0):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                yield matrix.get(pos + complex(dx, dy), default)


Part1()
Part2()
