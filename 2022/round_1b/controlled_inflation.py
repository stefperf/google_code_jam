# https://github.com/google/coding-competitions-archive/tree/main/codejam/2022/round_1b/controlled_inflation


from typing import Tuple


def solve(pressure_sets: Tuple[Tuple[int, ...], ...]) -> int:
    """
    >>> solve(((30, 10, 40), (20, 50, 60), (60, 60, 50)))
    110

    >>> solve(((1, 1000000000), (500000000, 1000000000), (1, 1000000000), (500000000, 1), (1, 1000000000)))
    4999999996
    """
    inc_last, dec_last, inc_minm, dec_minm = 0, 0, 0, 0
    for pressure_set in pressure_sets:
        minp, maxp = min(pressure_set), max(pressure_set)
        deltap = maxp - minp
        inc_minm_new = min(inc_minm + abs(inc_last - minp), dec_minm + abs(dec_last - minp)) + deltap
        dec_minm_new = min(inc_minm + abs(inc_last - maxp), dec_minm + abs(dec_last - maxp)) + deltap
        inc_last, dec_last, inc_minm, dec_minm = maxp, minp, inc_minm_new, dec_minm_new
    overall_min = min(inc_minm, dec_minm)
    return overall_min


if __name__ == "__main__":
    import doctest
    doctest.testmod()
