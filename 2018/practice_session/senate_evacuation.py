# https://github.com/google/coding-competitions-archive/blob/main/codejam/2018/practice_session/senate_evacuation


from collections import Counter
from sortedcontainers import SortedDict
from typing import List


class SortedMultiset:
    def __init__(self, counter=None):
        self.__counter = Counter()
        self.__sorted_by_count = SortedDict()
        self.__total_count = 0
        if counter:
            self.add_counter(counter)

    @property
    def distinct_count(self):
        return len(self.__counter)

    @property
    def total_count(self):
        return self.__total_count

    def add_counter(self, counter: Counter):
        for element, card in counter.items():
            self.add(element, card)

    def add(self, element, card=1):
        # Increment the element's and total count
        self.__counter[element] += card
        count = self.__counter[element]
        self.__total_count += card

        # Remove the element from the previous count bucket, if applicable
        if count > card:
            self.__sorted_by_count[count - card].remove(element)
            if not self.__sorted_by_count[count - card]:
                del self.__sorted_by_count[count - card]

        # Add the element to the higher count bucket
        if count not in self.__sorted_by_count:
            self.__sorted_by_count[count] = {element}
        else:
            self.__sorted_by_count[count].add(element)

    def remove(self, element, card=1):
        # Decrement the element's and total count
        if self.__counter[element] < card:
            return  # Element not numerous enough in multiset
        self.__counter[element] -= card
        count = self.__counter[element]
        self.__total_count -= card

        # Remove the element from its current count bucket
        self.__sorted_by_count[count + card].remove(element)
        if not self.__sorted_by_count[count + card]:
            del self.__sorted_by_count[count + card]

        # Add the element back to the lower count bucket, if applicable
        if count > 0:
            if count not in self.__sorted_by_count:
                self.__sorted_by_count[count] = {element}
            else:
                self.__sorted_by_count[count].add(element)
        else:
            del self.__counter[element]  # Completely remove if count is 0

    def get_elements_by_count(self):
        # Returns a list of tuples (count, elements) sorted by count
        return [(count, elements) for count, elements in self.__sorted_by_count.items()]

    def get_most_numerous_elements(self):
        # Returns the set of most numerous elements and their cardinality
        return self.__sorted_by_count.peekitem(-1)[1]

    def pop_one_with_max_count(self):
        # Pops one of the elements with max count
        element = next(self.get_most_numerous_elements())
        self.remove(element)
        return element

    def pop_first_with_max_count(self):
        # Pops the first of the elements with max count
        element = sorted(self.get_most_numerous_elements())[0]
        self.remove(element)
        return element


def solve(memberships: List[int]) -> List[str]:
    """
    >>> solve([2, 2])
    ['AB', 'AB']

    >>> solve([3, 2, 2])
    ['A', 'A', 'B', 'C', 'A', 'BC']

    >>> solve([1, 1, 2])
    ['C', 'A', 'BC']

    >>> solve([2, 3, 1])
    ['B', 'A', 'B', 'A', 'BC']
    """
    counter = Counter({chr(ord('A') + i): n for i, n in enumerate(memberships)})
    sms = SortedMultiset(counter)

    # choosing this deterministic method for easier testing,
    # although the non-deterministic pop_one_with_max_count would be more efficient
    pop = sms.pop_first_with_max_count

    steps = []
    while sms.distinct_count > 2:
        steps.append(pop())
    while sms.total_count > 0:
        steps.append("".join([pop(), pop()]))

    return steps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
