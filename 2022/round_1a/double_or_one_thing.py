# https://github.com/google/coding-competitions-archive/blob/main/codejam/2022/round_1a/double_or_one_thing


def solve(input_str: str):
    """
    >>> solve("PEEL")
    PEEEEL

    >>> solve("AAAAAAAAAA")
    AAAAAAAAAA

    >>> solve("CODEJAMDAY")
    CCODDEEJAAMDAAYdouble_or_one_thing.py
    """
    letters, counts = to_letter_counts(input_str)
    segments = [ch0 * count * (2 if ch0 < ch1 else 1)
            for ch0, ch1, count in zip(letters[:-1], letters[1:], counts[:-1])] + [letters[-1] * counts[-1]]
    output_str = "".join(segments)
    print(output_str)


def to_letter_counts(input_str):
    """
    >>> to_letter_counts("")
    ([], [])

    >>> to_letter_counts("h")
    (['h'], [1])

    >>> to_letter_counts("hello")
    (['h', 'e', 'l', 'o'], [1, 1, 2, 1])
    """
    letters = []
    counts = []
    if input_str:
        letters.append(input_str[0])
        counts.append(1)
        for ch in input_str[1:]:
            if ch != letters[-1]:
                letters.append(ch)
                counts.append(1)
            else:
                counts[-1] += 1
    return letters, counts


if __name__ == "__main__":
    import doctest
    doctest.testmod()
