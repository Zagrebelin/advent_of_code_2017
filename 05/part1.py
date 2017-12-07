import aocframe


class Part1(aocframe.AoCFramework):
    known_result = 343467

    def go(self):
        jumps = list(map(int, self.linesplitted))

        pos = 0
        st = 0
        try:
            while True:
                jmp = jumps[pos]
                jumps[pos] += 1
                pos += jmp
                st += 1
        except Exception:
            return st


class Part2(aocframe.AoCFramework):
    known_result = 24774780

    def go(self):
        jumps = list(map(int, self.linesplitted))

        pos = 0
        st = 0
        try:
            while True:
                jmp = jumps[pos]
                if jmp >= 3:
                    jumps[pos] -= 1
                else:
                    jumps[pos] += 1
                pos += jmp
                st += 1
        except Exception:
            return st


Part1()
Part2()
