# https://github.com/google/coding-competitions-archive/tree/main/codejam/2022/round_1a/weightlifting


from functools import lru_cache, reduce
from typing import Tuple


@lru_cache(maxsize=None)
def solve(msets: Tuple[Tuple[int, ...], ...]) -> int:
    """
    >>> solve(((0,),))
    0

    >>> solve(((3,),))
    6

    >>> solve(((1, 4, 2),))
    14

    >>> solve(((1,), (2,), (1,)))
    4

    >>> solve(((0, 0), (0, 0)))
    0

    >>> solve(((1, 2, 1), (2, 1, 2)))
    12

    >>> solve(((3, 1, 1), (3, 3, 3), (2, 3, 3)))
    20

    >>> solve(((0, 1, 4), (2, 5, 6), (1, 4, 1)))
    32
    """
    bottom_weights = min_mset(msets)
    modified_msets = tuple(map(lambda x: diff_mset(x, bottom_weights), msets))

    recursive_res = 0 if all(sum(mms) == 0 for mms in modified_msets) else split(modified_msets)

    min_ops = 2 * sum(bottom_weights) + recursive_res

    return min_ops


def split(msets: Tuple[Tuple[int, ...], ...]) -> int:
    n = len(msets)
    possible_min_ops = [solve(msets[:s]) + solve(msets[s:]) for s in range(1, n)]
    min_ops = min(possible_min_ops)
    return min_ops


@lru_cache(maxsize=None)
def min_mset(msets: Tuple[Tuple[int, ...], ...]) -> Tuple[int, ...]:
    """
    >>> min_mset(((1, 2, 3), (3, 0, 5), (2, 2, 2)))
    (1, 0, 2)
    """
    return reduce(lambda x, y: tuple((min(xi, yi) for xi, yi in zip(x, y))), msets)


def diff_mset(mset1: Tuple[int, ...], mset0: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    >>> diff_mset((3, 5, 2), (2, 5, 0))
    (1, 0, 2)
    """
    return tuple((e1 - e0 for e1, e0 in zip(mset1, mset0)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
