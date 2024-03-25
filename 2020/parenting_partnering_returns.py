# https://github.com/google/coding-competitions-archive/blob/main/codejam/2020/qualification_round/parenting_partnering_returns


from dataclasses import dataclass, replace
from itertools import product
from typing import List


@dataclass
class Act:
    beg: int
    end: int
    index: int = None


def solve(activities: List[Act]) -> str:
    """
    >>> solve([Act(360, 480), Act(420, 540), Act(600, 660)]) in ['CJC', 'JCJ']
    True

    >>> solve([Act(0, 1440), Act(1, 3), Act(2, 4)])
    'IMPOSSIBLE'

    >>> solve([Act(99, 150), Act(1, 100), Act(100, 301), Act(2, 5), Act(150, 250)]) in ['JCCJJ', 'CJJCC']
    True

    >>> solve([Act(0, 720), Act(720, 1440)]) in ['CC', 'JJ']
    True
    """
    # return naive_solve(activities)

    # smarter implementation
    indexed_activities = [replace(a, index=i) for i, a in enumerate(activities)]
    sorted_activities = sorted(indexed_activities, key=lambda a: a.beg)

    # Cameron's activities and the time his last activity ends
    c_activities, c_end = [sorted_activities[0]], sorted_activities[0].end
    # Jamie's activities and the time his last activity ends
    j_activities, j_end = [], 0
    for activity in sorted_activities[1:]:
        if c_end <= activity.beg:
            c_activities.append(activity)
            c_end = activity.end
        elif j_end <= activity.beg:
            j_activities.append(activity)
            j_end = activity.end
        else:
            return 'IMPOSSIBLE'

    schedule = ['C' for _ in range(len(activities))]
    for a in j_activities:
        schedule[a.index] = 'J'
    return ''.join(schedule)


def naive_solve(activities: List[Act]) -> str:
    for schedule in product(*['CJ' for _ in range(len(activities))]):
        c_activities = []
        j_activities = []
        for s, a in zip(schedule, activities):
            if s == 'C':
                c_activities.append(a)
            else:
                j_activities.append(a)
        if feasible_schedule(c_activities) and feasible_schedule(j_activities):
            return ''.join(schedule)
    return 'IMPOSSIBLE'


def feasible_schedule(activities: List[Act]) -> bool:
    """
    >>> feasible_schedule([])
    True

    >>> feasible_schedule([Act(1, 2)])
    True

    >>> feasible_schedule([Act(2, 4), Act(1, 2), Act(5, 7)])
    True

    >>> feasible_schedule([Act(2, 4), Act(1, 3), Act(5, 7)])
    False
    """
    sorted_activities = sorted(activities, key=lambda a: a.beg)
    overlaps = [a0.end > a1.beg for a0, a1 in zip(sorted_activities[:-1], sorted_activities[1:])]
    return not any(overlaps)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
