# https://github.com/google/coding-competitions-archive/blob/main/codejam/2020/qualification_round/nesting_depth


def solve(input_str: str) -> str:
    """
    >>> solve('021')
    '0((2)1)'

    >>> solve('312')
    '(((3))1(2))'

    >>> solve('4')
    '((((4))))'

    >>> solve('221')
    '((22)1)'
    """
    # return elide_parentheses(add_parentheses(input_str))  # naive solution
    return add_min_parentheses('0' + input_str + '0')[1:-1]


def add_min_parentheses(standard_input_str: str) -> str:
    return ''.join([standard_input_str[0]] +
           [parentheses_between(int(d0), int(d1)) + d1
            for d0, d1 in zip(standard_input_str[:-1], standard_input_str[1:])])


def parentheses_between(x: int, y: int) -> str:
    """
    >>> parentheses_between(6, 6)
    ''

    >>> parentheses_between(6, 9)
    '((('

    >>> parentheses_between(6, 5)
    ')'
    """
    diff = int(y) - int(x)
    if diff == 0:
        return ''
    else:
        return ('(' if diff > 0 else ')') * abs(diff)


def add_parentheses(input_str: str) -> str:
    """
    >>> add_parentheses('1202310')
    '(1)((2))0((2))(((3)))(1)0'
    """
    return ''.join('(' * int(digit) + digit + ')' * int(digit) for digit in input_str)


def elide_parentheses(input_str: str) -> str:
    """
    elide_parentheses('(1)((2))0((2))(((3)))(1)0')
    '(1(2))0((2(3))1)0'
    """
    output_str = input_str
    for _ in range(9):
        output_str = output_str.replace(')(', '')
    return output_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
