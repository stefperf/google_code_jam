# https://github.com/google/coding-competitions-archive/blob/main/codejam/2018/practice_session/bathroom_stalls


from collections import Counter
from functools import lru_cache
from typing import Tuple


def solve(n: int, k: int) -> Tuple[int, int]:
    """
    >>> solve(1000000000000000000, 281333243177482637)
    (2, 2)

    >>> solve(4, 2)
    (1, 0)

    >>> solve(5, 2)
    (1, 0)

    >>> solve(6, 2)
    (1, 1)

    >>> solve(1000, 1000)
    (0, 0)

    >>> solve(1000, 1)
    (500, 499)

    >>> solve(254, 206)
    (0, 0)
    """
    # min_, max_ = rec_eval(n, k)
    # return max_, min_
    return mset_eval(n, k)


def mset_eval(n: int, k: int) -> Tuple[int, int]:
    mset = Counter({n: 1})
    while k > 0:
        max_seq = max(mset.keys())
        card = mset[max_seq]
        step = min(k, card)
        n1, n2 = residuals(max_seq)
        k -= step
        if k == 0:
            return n2, n1
        mset[max_seq] -= step
        if mset[max_seq] == 0:
            del mset[max_seq]
        mset[n1] += step
        mset[n2] += step


@lru_cache(maxsize=None)
def rec_eval(n: int, k: int) -> Tuple[int, int]:
    if k > n // 2:
        return 0, 0
    elif k == 1:
        return residuals(n)
    elif k == 2:
        _, n2 = residuals(n)
        return residuals(n2)
    else:
        n1, n2 = residuals(n)
        k1, k2 = residuals(k)
        results = [rec_eval(n1, k1), rec_eval(n2, k2)]
        best_res = sorted(results)[1]
        return best_res


def residuals(i: int) -> Tuple[int, int]:
    """
    Return floor((i - 1) / 2), ceil((i - 1) / 2). Input i must be > 0.

    >>> residuals(1)
    (0, 0)

    >>> residuals(2)
    (0, 1)

    >>> residuals(3)
    (1, 1)

    >>> residuals(4)
    (1, 2)
    """
    floored_half = i // 2
    if i % 2 == 0:
        return floored_half - 1, floored_half
    else:
        return floored_half, floored_half


if __name__ == "__main__":
    import doctest
    doctest.testmod()
