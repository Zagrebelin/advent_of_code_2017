"""
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is,
where the result of the division operation is a whole number. They would like you to find those numbers on each line,
divide them, and add up each line's result.
"""
import itertools

data = open('data//day_02').read()
ch = 0
for line in data.split('\n'):
    digits = list(map(int, line.split()))
    for a, b in itertools.product(digits, digits):
        if a == b:
            continue
        if a % b == 0:
            ch += a // b
            break

print(ch)
