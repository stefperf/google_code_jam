# https://github.com/google/coding-competitions-archive/blob/main/codejam/2022/qualification_round/3d_printing

from typing import List


N_COLORS = 4


def solve(printers: List[List[int]], needed_units: int = 1000000) -> List[int]:
    """

    :param printers:
    :param needed_units:
    :return:

    >>> solve([[0, 0, 9, 9], [9, 9, 0, 0], [3, 6, 4, 5]], 10)
    []

    >>> solve([[1, 7, 5, 9], [5, 2, 8, 6], [4, 6, 0, 3]], 10)
    []

    >>> solve([[1, 7, 5, 9], [5, 2, 8, 6], [4, 6, 7, 3]], 10)
    [1, 2, 5, 2]
    """
    n_printers = len(printers)
    mins: List[int] = [min([printers[p][c] for p in range(n_printers)]) for c in range(N_COLORS)]
    if sum(mins) < needed_units:
        return []
    else:
        result: List[int] = []
        still_needed_units: int = needed_units
        for color, min_color in zip(printers[0], mins):
            color_used = min((color, min_color, still_needed_units))
            still_needed_units -= color_used
            result.append(color_used)
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
