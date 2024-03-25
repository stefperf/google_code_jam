# https://github.com/google/coding-competitions-archive/blob/main/codejam/2021/qualification_round/reversort


from typing import List, Tuple


def solve(els: List[int]) -> int:
    """
    >>> solve([4, 2, 1, 3])
    6

    >>> solve([1, 2])
    1

    >>> solve([7, 6, 5, 4, 3, 2, 1])
    12
    """
    return reversort(els)[1]  # naive implementation


def reversort(els: List[int]) -> (List[int], int):
    """
    Sort els by reversort; return sorted els and total cost.
    els are assumed to be always non-empty and distict.

    >>> reversort([1])
    ([1], 0)

    >>> reversort([1, 2])
    ([1, 2], 1)

    >>> reversort([3, 2])
    ([2, 3], 2)
    """
    end_pos = len(els) - 1
    cost = 0
    for i in range(0, end_pos):
        j = find_min_pos(els, i, end_pos)
        cost += j - i + 1
        els[i:j + 1] = els[i:j + 1][::-1]
        # print(els)
    return els, cost


def find_min_pos(els, beg_pos, end_pos):
    """
    Find the position of the min el in els between beg_pos and end_pos included.
    els are assumed to be always non-empty and distict, with valid beg_pos and end_pos.

    >>> find_min_pos([1], 0, 0)
    0

    >>> find_min_pos([1, 2], 0, 1)
    0

    >>> find_min_pos([1, 0], 0, 1)
    1

    >>> find_min_pos([7, 1], 1, 1)
    1

    >>> find_min_pos([7, 1, 2], 1, 2)
    1

    >>> find_min_pos([7, 1, 0], 1, 2)
    2
    """
    pos, min_pos, min_el = beg_pos, beg_pos, els[beg_pos]
    while pos < end_pos:
        pos += 1
        el = els[pos]
        if el < min_el:
            min_pos, min_el = pos, el
    return min_pos



if __name__ == "__main__":
    import doctest
    doctest.testmod()
