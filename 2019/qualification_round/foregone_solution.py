# https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/qualification_round/foregone_solution


from typing import Tuple


def solve(n: int) -> Tuple[int, int]:
    """
    >>> test(solve(4), 4)
    True

    >>> test(solve(940), 940)
    True

    >>> test(solve(4444), 4444)
    True

    >>> test(solve(1324444), 1324444)
    True

    >>> test(solve(132444479), 132444479)
    True
    """
    n_str = str(n)
    try:
        index_of_first_four = n_str.index('4')
        o_str = ''.join(['1' if digit == '4' else '0' for digit in n_str[index_of_first_four:]])
        o = int(o_str)
        p = n - o
        return o, p
    except ValueError:
        return n, 0


def test(addends: Tuple[int, int], n: int) -> bool:
    """
    >>> test((10, 34), 44)
    False

    >>> test((14, 30), 44)
    False

    >>> test((10, 33), 44)
    False

    >>> test((11, 33), 44)
    True
    """
    return addends[0] + addends[1] == n and '4' not in str(addends[0]) and '4' not in str(addends[1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
