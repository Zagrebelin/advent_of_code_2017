import itertools


def is_valid(ph):
    words = ph.strip().split()
    uniq = set(words)
    return len(uniq) == len(words)


def is_valid2(ph):
    def is_eq(w1, w2):
        l1 = list(sorted(w1))
        l2 = list(sorted(w2))
        return l1 == l2

    words = ph.strip().split()
    for w1, w2 in itertools.combinations(words, 2):
        if is_eq(w1, w2):
            return False
    return True


assert is_valid('aa bb cc dd ee')
assert not is_valid('aa bb cc dd aa')
assert is_valid('aa bb cc dd aaa')

assert is_valid2('abcde fghij')
assert not is_valid2('abcde xyz ecdab')
assert is_valid2('a ab abc abd abf abj')
assert is_valid2('iiii oiii ooii oooi oooo')
assert not is_valid2('oiii ioii iioi iiio')
print('assert ok.')

data = open('data/day_04.txt').read().split('\n')

print(sum(map(is_valid, data)))
print(sum(map(is_valid2, data)))