# https://github.com/google/coding-competitions-archive/blob/main/codejam/2018/qualification_round/saving_the_universe_again


from typing import Optional


def solve(max_damage: int, instr_seq: str) -> Optional[int]:
    """
    >>> solve(1, 'CS')
    1

    >>> solve(2, 'CS')
    0

    >>> solve(1, 'SS') is None
    True

    >>> solve(6, 'SCCSSC')
    2

    >>> solve(2, 'CC')
    0

    >>> solve(3, 'CSCSS')
    5
    """
    n_swaps = 0
    while True:
        if eval_damage(instr_seq) <= max_damage:
            return n_swaps
        else:
            # search for the next best swap; try it if it exists, otherwise recognize that the problem is impossible
            last_cs_pos = instr_seq.rfind('CS')
            if last_cs_pos >= 0:
                instr_seq = swap(instr_seq, last_cs_pos)
                n_swaps += 1
            else:
                return None


def naive_solve(max_damage: int, instr_seq: str) -> Optional[int]:
    """
    >>> naive_solve(1, 'CS')
    1

    >>> naive_solve(2, 'CS')
    0

    >>> naive_solve(1, 'SS') is None
    True

    >>> naive_solve(6, 'SCCSSC')
    2

    >>> naive_solve(2, 'CC')
    0

    >>> naive_solve(3, 'CSCSS')
    5
    """
    # init
    n = len(instr_seq)

    n_swaps = 0
    new_seqs = [instr_seq]
    all_seen_seqs = set(new_seqs)

    # iterate until new seqs can be found
    while new_seqs:
        # test all new latest found new seqs
        for s in new_seqs:
            if eval_damage(s) <= max_damage:
                return n_swaps

        # try to find more new seqs by executing one more swap
        n_swaps += 1
        last_seqs = new_seqs
        new_seqs = []
        for s in last_seqs:
            for pos in range(n - 1):
                maybe_new_s = swap(s, pos)
                if maybe_new_s not in all_seen_seqs:
                    all_seen_seqs.add(maybe_new_s)
                    new_seqs.append(maybe_new_s)

    # admit impossibility if all possible seqs have been tested in vain
    return None


def eval_damage(instr_seq: str) -> int:
    """
    >>> eval_damage('SCSCSC')
    7
    """
    total_value = 0
    curr_value = 1
    for i in instr_seq:
        if i == 'S':
            total_value += curr_value
        else:
            curr_value *= 2
    return total_value


def swap(instr_seq: str, pos: int) -> str:
    """
    >>> swap('SCSC', 0)
    'CSSC'

    >>> swap('SCSC', 1)
    'SSCC'

    >>> swap('SCSC', 2)
    'SCCS'
    """
    return (instr_seq[:pos] + ''.join([instr_seq[pos + 1], instr_seq[pos]])) + instr_seq[pos + 2:]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
