from collections import defaultdict

from aocframe import AoCFramework
import operator

OPS = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    'inc': operator.add,
    'dec': operator.sub
}


class Part1(AoCFramework):
    test_cases = [('''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10''', 1)]
    known_result = 2971

    def go(self, data: str):
        regs = defaultdict(int)
        for line in data.splitlines():
            reg_a, op_a, value_a, _, reg_if, op_if, value_if = line.split()
            value_a = int(value_a)
            op_a = OPS[op_a]

            value_if = int(value_if)
            op_if = OPS[op_if]

            if op_if(regs[reg_if], value_if):
                regs[reg_a] = op_a(regs[reg_a], value_a)
        return max(regs.values())


class Part2(AoCFramework):
    known_result = 4254

    def go(self, data: str):
        regs = defaultdict(int)
        ret = 0
        for line in data.splitlines():
            reg_a, op_a, value_a, _, reg_if, op_if, value_if = line.split()
            value_a = int(value_a)
            op_a = OPS[op_a]

            value_if = int(value_if)
            op_if = OPS[op_if]

            if op_if(regs[reg_if], value_if):
                regs[reg_a] = op_a(regs[reg_a], value_a)
                ret = max(ret, regs[reg_a])
        return ret


Part1()
Part2()
