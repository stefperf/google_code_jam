# https://github.com/google/coding-competitions-archive/blob/main/codejam/2020/qualification_round/vestigium


from typing import List, Tuple


def solve(square: List[List[int]]) -> Tuple[int, int, int]:
    """
    >>> solve([[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]])
    (4, 0, 0)

    >>> solve([[2, 2, 2, 2], [2, 3, 2, 3], [2, 2, 2, 3], [2, 2, 2, 2]])
    (9, 4, 4)

    >>> solve([[2, 1, 3], [1, 3, 2], [1, 2, 3]])
    (8, 0, 2)
    """
    size = len(square)

    trace = sum(square[i][i] for i in range(size))

    r = sum(0 if len(set(row)) == size else 1 for row in square)

    cols = [[square[r][c] for r in range(size)] for c in range(size)]
    c = sum(0 if len(set(col)) == size else 1 for col in cols)

    return trace, r, c


if __name__ == "__main__":
    import doctest
    doctest.testmod()
