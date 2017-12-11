from aocframe import AoCFramework


class Part1(AoCFramework):
    test_cases = [
        ['{}', 1],
        ['{{{}}}', 6],
        ['{{},{}}', 5],
        ['{{{},{},{{}}}}', 16],
        ['{<a>,<a>,<a>,<a>}', 1],
        ['{{<ab>},{<ab>},{<ab>},{<ab>}}', 9],
        ['{{<!!>},{<!!>},{<!!>},{<!!>}}', 9],
        ['{{<a!>},{<a!>},{<a!>},{<ab>}}', 3],
    ]
    known_result = 9662

    def go(self, data: str):
        in_garbage = False
        ignore = False
        depth = 0
        ret = 0
        for c in data:
            if c == '<' and not ignore:
                in_garbage = True
            elif c == '>' and not ignore:
                in_garbage = False
            elif c == '!' and in_garbage and not ignore:
                ignore = True
            elif in_garbage and ignore:
                ignore = False
                continue
            elif c == '{' and not in_garbage:
                depth += 1
            elif c == '}' and not in_garbage:
                ret += depth
                depth -= 1
            else:
                continue
        return ret


class Part2(AoCFramework):
    test_cases = [
        ['<>', 0],
        ['<random characters>', 17],
        ['<<<<>', 3],
        ['<{!>}>', 2],
        ['<!!>', 0],
        ['<!!!>>', 0],
        ['<{o"i!a,<{i<a>', 10],
    ]

    def go(self, data: str):
        in_garbage = False
        ignore = False
        depth = 0
        ret = 0
        for c in data:
            if c == '<' and not ignore and not in_garbage:
                in_garbage = True
            elif c == '>' and not ignore:
                in_garbage = False
            elif c == '!' and in_garbage and not ignore:
                ignore = True
            elif in_garbage and ignore:
                ignore = False
                continue
            elif in_garbage:
                ret +=1
        return ret


Part1()
Part2()
