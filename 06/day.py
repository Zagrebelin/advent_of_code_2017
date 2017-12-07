from aocframe import AoCFramework


class Part1(AoCFramework):
    known_result = 5042
    test_cases = [('0 2 7 0', 5)]

    def go(self, data):
        banks = list(map(int, data.split()))
        seen = []
        step = 0
        while True:
            step += 1
            seen.append(tuple(banks))
            bank_from = max((value, -1 * idx) for idx, value in enumerate(banks))[1] * (-1)
            distribute = banks[bank_from]
            banks[bank_from] = 0
            bank_to = (bank_from + 1) % len(banks)
            while distribute > 0:
                banks[bank_to] += 1
                distribute -= 1
                bank_to = (bank_to + 1) % len(banks)
            if tuple(banks) in seen:
                return step
            seen.append(banks)


class Part2(AoCFramework):
    known_result = 1086
    test_cases = [ ('2 4 1 2', 4)]

    def go(self, data):
        banks = list(map(int, data.split()))
        seen = []
        step = 0
        while True:
            step += 1
            seen.append(tuple(banks))
            bank_from = max((value, -1 * idx) for idx, value in enumerate(banks))[1] * (-1)
            distribute = banks[bank_from]
            banks[bank_from] = 0
            bank_to = (bank_from + 1) % len(banks)
            while distribute > 0:
                banks[bank_to] += 1
                distribute -= 1
                bank_to = (bank_to + 1) % len(banks)
            t = tuple(banks)
            if t in seen:
                return len(seen)-seen.index(t)


Part1()
print()
Part2()