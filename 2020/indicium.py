# https://github.com/google/coding-competitions-archive/blob/main/codejam/2020/qualification_round/indicium


from itertools import permutations


def solve(n, k):
    """
    >>> solve(3, 6)
    [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

    >>> latin_square_is_ok(solve(3, 6), 3, 6)
    True

    >>> solve(2, 3) is None
    True

    >>> latin_square_is_ok(solve(4, 12), 4, 12)
    True
    """
    trace, latin_square = -1, None
    for latin_square in permutations(get_base_latin_square(n)):
        trace = get_trace(latin_square)
        if trace == k:
            break
    return list(latin_square) if trace == k else None


def latin_square_is_ok(candidate_square, size, trace):
    """
    >>> latin_square_is_ok([[1]], 1, 1)
    True

    >>> latin_square_is_ok([[1, 2], [1, 2]], 2, 3)
    False
    """
    if len(candidate_square) != size or any((len(row) != size for row in candidate_square)):
        return False
    if get_trace(candidate_square) != trace:
        return False

    sorted_row = sorted(range(1, size + 1))

    def rows_are_latin(rows):
        return all((all(er == es for er, es in zip(sorted(row), sorted_row)) for row in rows))

    if not rows_are_latin(candidate_square):
        return False

    if not rows_are_latin(transpose(candidate_square)):
        return False

    return True


def get_base_latin_square(n):
    """
    >>> get_base_latin_square(1)
    [[1]]

    >>> get_base_latin_square(2)
    [[1, 2], [2, 1]]


    >>> get_base_latin_square(3)
    [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    """
    row = list(range(1, n + 1))
    rows = [row.copy()]
    for r in range(n - 1):
        row = [row[-1]] + row[:-1]
        rows.append(row.copy())
    return rows


def get_trace(square):
    """
    >>> get_trace([[1]])
    1

    >>> get_trace([[2, 3, 1], [3, 1, 2], [1, 2, 3]])
    6
    """
    return sum((square[i][i] for i in range(len(square))))


def transpose(square):
    """
    >>> transpose([[1]])
    [[1]]

    >>> transpose([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    [[1, 3, 2], [2, 1, 3], [3, 2, 1]]
    """
    size = len(square)
    return [[square[j][i] for j in range(size)] for i in range(size)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
