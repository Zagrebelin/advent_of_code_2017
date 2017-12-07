import re

import itertools

from aocframe import AoCFramework

class Part1(AoCFramework):
    known_result = 'eugwuhl'
    def go(self, data: str):
        rests = []
        firsts = []
        for x in data.splitlines():
            names = re.findall(r'\b\w+\b',x)
            first, *rest = names
            rests += rest
            firsts.append(first)
        for f in firsts:
            if f not in rests:
                return f




class Part2(AoCFramework):
    test_cases = [
        ('''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)''', 60)

    ]
    known_result = 420

    def go(self, data: str):
        self.children_struct = {}
        self.weights = {}
        for x in data.splitlines():
            names_in_str = re.findall(r'\b[a-z]+\b',x)
            weight_in_str = int(re.findall(r'\d+', x)[0])
            name, *this_children = names_in_str
            self.weights[name] = weight_in_str
            self.children_struct[name] = this_children
        all_children = list(itertools.chain(*self.children_struct.values()))
        root = [f for f in self.children_struct.keys() if f not in all_children][0]
        return self.find_differ(root)

    def calculate_weight(self, name):
        ret = self.weights[name]
        for child in self.children_struct.get(name, []):
            ret += self.calculate_weight(child)
        return ret

    def find_differ(self, root):
        """
        ищем разницу в поддеревьях какого-то листа.
        считаем сумму весов поддеревьев листа. Если она разная, то ныряем в ту ветку, которая различается и считаем там.
        Если все ветки одинакоыв, значит ошибка на нашем уровне и балансируемся тут.

        :param root:
        :return:
        """
        children_of_root_weights = [(child, self.calculate_weight(child)) for child in self.children_struct[root]]
        if len(set(t[1] for t in children_of_root_weights)) == 1:
            return None
        heavy_name, heavy_weight = max(children_of_root_weights, key=lambda x:x[1])
        error_in_child = self.find_differ(heavy_name)
        if error_in_child is None:
            _, easy_weight = min(children_of_root_weights, key=lambda x:x[1])
            diff = heavy_weight-easy_weight
            return self.weights[heavy_name] - diff
        else:
            return error_in_child




# 4608



# Part1()
Part2()