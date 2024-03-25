# https://github.com/google/coding-competitions-archive/blob/main/codejam/2022/qualification_round/chain_reactions

from itertools import permutations
from typing import List, Set


class Module:
    def __init__(self, fun: int, next: int):
        self.fun = fun
        self.next = next
        self.active = True


class Machine:
    def __init__(self, n_modules: int, funs: List[int], nexts: List[int]):
        self.triggers: Set[int] = set(range(0, n_modules))
        self.modules: List[Module] = []
        for i, (fun, next) in enumerate(zip(funs, nexts)):
            module = Module(fun, next - 1)
            self.modules.append(module)
            next_ = next - 1
            if next_ >= 0 and next_ in self.triggers:
                self.triggers.remove(next_)

    def reset_modules(self):
        for module in self.modules:
            module.active = True

    def chain(self, trigger) -> int:
        module = self.modules[trigger]
        module.active = False
        if module.next < 0 or self.modules[module.next].active == False:
            return module.fun
        else:
            return max(module.fun, self.chain(module.next))

    def fun(self, trigger_sequence):
        self.reset_modules()
        total_fun = 0
        for trigger in trigger_sequence:
            total_fun += self.chain(trigger)
        return total_fun

    def max_fun(self):
        max_fun_possible = 0
        for trigger_sequence in permutations(self.triggers):
            total_fun = self.fun(trigger_sequence)
            max_fun_possible = max(max_fun_possible, total_fun)
        return max_fun_possible


def solve(n_modules: int, funs: List[int], nexts: List[int]) -> int:
    """
    :param n_modules:
    :param funs:
    :param nexts:
    :return:

    >>> solve(4, [60, 20, 40, 50], [0, 1, 1, 2])
    110
    """
    machine = Machine(n_modules, funs, nexts)
    return machine.max_fun()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
