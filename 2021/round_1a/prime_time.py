# https://github.com/google/coding-competitions-archive/blob/main/codejam/2021/round_1a/prime_time


from itertools import product
from typing import List


def solve(primes: List[int], counts: List[int]) -> int:
    """
    >>> solve([2, 3, 5, 7, 11], [2, 1, 2, 1, 1])
    25

    >>> solve([17], [2])
    17

    >>> solve([2, 3], [2, 1])
    0

    >>> solve([2], [7])
    8
    """
    n_primes = len(primes)

    count_choices = [list(range(0, c + 1)) for c in counts]
    choice_sets = product(*count_choices)

    max_score = 0
    for choice_set in choice_sets:
        rest_set = [count - choice for count, choice in zip(counts, choice_set)]

        possible_sum = sum([prime * choice for prime, choice in zip(primes, choice_set)])

        possible_factors = sorted([prime ** choice for prime, choice in zip(primes, rest_set)], reverse=True)
        possible_prod = 1
        for possible_factor in possible_factors:
            if possible_sum >= possible_prod:
                possible_prod *= possible_factor
            else:
                break

        if possible_sum == possible_prod and possible_sum > max_score:
            max_score = possible_sum

    return max_score


if __name__ == "__main__":
    import doctest
    doctest.testmod()
