# https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/qualification_round/you_can_go_your_own_way


from typing import List, Tuple


def solve(lydias_path: str) -> str:
    """
    >>> test('ES', solve('ES'))
    True

    >>> test('SEEESSES', solve('SEEESSES'))
    True
    """
    return ''.join(['S' if move == 'E' else 'E' for move in lydias_path])


def test(lydias_path: str, my_path: str) -> bool:
    """
    >>> test('SSEE', 'SESE')
    False

    >>> test('ESES', 'SESE')
    True
    """
    lydias_move_set = set(path2moves(lydias_path))
    my_move_set = set(path2moves(my_path))
    return not lydias_move_set.intersection(my_move_set)


def path2moves(path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    >>> path2moves('SESSEE')
    [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (3, 1)), ((3, 1), (3, 2)), ((3, 2), (3, 3))]
    """
    moves = [((0, 0), (0, 1)) if path[0] == 'E' else ((0, 0), (1, 0))]
    for move in path[1:]:
        pos0 = moves[-1][1]
        pos1 = (pos0[0], pos0[1] + 1) if move == 'E' else (pos0[0] + 1, pos0[1])
        moves.append((pos0, pos1))
    return moves


if __name__ == "__main__":
    import doctest
    doctest.testmod()
