# https://github.com/google/coding-competitions-archive/blob/main/codejam/2022/qualification_round/d1000000

from typing import List


def solve(dice: List[int]) -> int:
    """
    Max straight length on given dice
    :param dice: max numbers of all dice
    :return: length of max straight

    >>> solve([])
    0

    >>> solve([1])
    1

    >>> solve([10])
    1

    >>> solve([1, 2, 3, 4])
    4

    >>> solve([6, 10, 12, 8])
    4

    >>> solve([5, 4, 5, 4, 4, 4])
    5

    >>> solve([10, 10, 7, 6, 7, 4, 4, 5, 7, 4])
    9
    """
    sorted_dice = sorted(dice)
    max_len = 0
    while len(sorted_dice) > max_len:
        max_len = max(max_len, max_from_first(sorted_dice))
        sorted_dice = sorted_dice[1:]
    return max_len


def max_from_first(sorted_dice: List[int]) -> int:
    """
    Max straight length when starting on the first dice with any possible number
    :param sorted_dice: increasingly sorted max numbers of all dice
    :return: length of max straight
    """
    return max_with_start(sorted_dice, 1)


def max_with_start(sorted_dice: List[int], start: int) -> int:
    """
    Max straight length when starting with number start on the first dice
    :param sorted_dice: increasingly sorted max numbers of all dice
    :param start: first number of a straight starting on the first die
    :return: length of max straight

    >>> max_with_start([2, 3, 3, 6], 3)
    0

    >>> max_with_start([2, 3, 3, 6], 1)
    4

    >>> max_with_start([2, 3, 3, 6], 2)
    2
    """
    number = start
    length = 0
    for die in sorted_dice:
        if number > die:
            break
        else:
            length += 1
        number += 1
    return length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
