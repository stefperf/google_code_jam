# https://gi thub.com/google/coding-competitions-archive/blob/main/codejam/2018/practice_session/steed_2_cruise_control


from typing import List


def solve(destination: float, horse_positions: List[float], horse_speeds: List[float]) -> float:
    """
    >>> abs(solve(2525, [2400], [5]) - 101) < 1e-6
    True

    >>> abs(solve(300, [120, 60], [60, 90]) - 100) < 1e-6
    True

    >>> abs(solve(100, [80, 70], [100, 10]) - 33.3333333) < 1e-6
    True
    """
    horse_times_to_destination = [(destination - p) / s for p, s in zip(horse_positions, horse_speeds)]
    return destination / max(horse_times_to_destination)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
