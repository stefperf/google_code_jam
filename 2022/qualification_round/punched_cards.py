# https://github.com/google/coding-competitions-archive/tree/main/codejam/2022/qualification_round/punched_cards

from typing import List


def solve(r: int, c: int):
    """
    solution
    :param r: row count
    :param c: col count
    :return: punch card as ASCII art

    >>> solve(2, 2)
    ..+-+
    ..|.|
    +-+-+
    |.|.|
    +-+-+

    >>> solve(3, 4)
    ..+-+-+-+
    ..|.|.|.|
    +-+-+-+-+
    |.|.|.|.|
    +-+-+-+-+
    |.|.|.|.|
    +-+-+-+-+
    """
    r_ = r - 1
    c_ = c - 1
    row0 = "..+" + "-+" * c_
    row1 = "..|" + ".|" * c_
    row2 = "+" + "-+" * c
    row3 = "|" + ".|" * c
    rows = [row0, row1, row2] + [row3, row2] * r_
    ascii_art = "\n".join(rows)
    print(ascii_art)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
