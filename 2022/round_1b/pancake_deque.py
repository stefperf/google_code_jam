# https://github.com/google/coding-competitions-archive/blob/main/codejam/2022/round_1b/pancake_deque


from collections import deque
from typing import Tuple


def solve(levels: Tuple[int, ...]) -> int:
    """
    >>> solve(())
    0

    >>> solve((4,))
    1

    >>> solve((1, 5))
    2

    >>> solve((1, 4, 2, 3))
    3

    >>> solve((7, 1, 3, 1000000))
    2
    """
    if len(levels) <= 1:
        return len(levels)

    deq, last_level, count = deque(levels), 0, 0
    while True:
        np = next_pop(deq, last_level)
        if np is None:
            break
        else:
            count += 1
            if np == 0:
                last_level = deq.popleft()
            else:
                last_level = deq.pop()

    return count


def next_pop(seq, min_val):
    """
    Choose the minimum extreme of seq which is >= min_val, if one can be found, returning:
    0 for the first value, -1 for the last value, None for none.

    >>> next_pop([], 0) is None
    True

    >>> next_pop([0], 1) is None
    True

    >>> next_pop([1], 1)
    0

    >>> next_pop([3, 5], 6) is None
    True

    >>> next_pop([3, 5], 5)
    -1

    >>> next_pop([5, 3], 5)
    0

    >>> next_pop([3, 5], 3)
    0

    >>> next_pop([5, 3], 3)
    -1
    """
    candidates = valid_extremes(seq, min_val)
    if not candidates:
        return None
    elif len(candidates) == 1:
        return candidates[0][1]
    elif candidates[0][0] < candidates[1][0]:
        return candidates[0][1]
    else:
        return candidates[1][1]

def valid_extremes(seq, min_val):
    """
    return the extremes of seq being >= min_val, if any, sorted by position

    >>> valid_extremes([], 0)
    []

    >>> valid_extremes([0], 1)
    []

    >>> valid_extremes([0, 1], 2)
    []

    >>> valid_extremes([0, 1], 1)
    [(1, -1)]

    >>> valid_extremes([1, 0], 1)
    [(1, 0)]

    >>> valid_extremes([1, 0], 0)
    [(1, 0), (0, -1)]
    """
    res = []
    length = len(seq)
    if length > 0 and seq[0] >= min_val:
        res.append((seq[0], 0))
    if length > 1 and seq[-1] >= min_val:
        res.append((seq[-1], -1))
    return res



if __name__ == "__main__":
    import doctest
    doctest.testmod()
