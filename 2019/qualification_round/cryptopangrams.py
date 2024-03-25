# https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/qualification_round/cryptopangrams


from typing import List


def solve(max_n: int, numbers: List[int]) -> str:
    """
    >>> solve(103, [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053])
    'CJQUIZKNOWBEVYOFDPFLUXALGORITHMS'

    >>> solve(152, [3337, 3337, 3337, 3337, 5041, 3337, 1739, 5069, 13289, 12707, 16637, 5207, 1271, 2449, 2449, 2449, 2449, 2449, 2449, 2449, 11929, 11929, 11929, 11929, 11929, 8909, 8909, 8909, 8909, 8909, 8909, 8909, 6077, 10403, 14039, 11537, 5561, 7571, 10057, 5429, 6527, 5671, 2279, 3139, 7957, 16241, 16241, 16241, 16241, 16241])
    'JEJEJJEBWOVUCALALALALZLZLZGZGZGZGQPXMITNHRFDKSYSYSY'
    """
    if numbers[0] != numbers[1]:
        prime_seq = process_good_seq(numbers)
    else:
        index_of_first_different_number = next((i for i, n in enumerate(numbers) if n != numbers[0]))
        forward_good_seq = numbers[index_of_first_different_number:]
        forward_prime_seq = process_good_seq(forward_good_seq)
        backward_good_seq = numbers[:index_of_first_different_number + 1][::-1]
        backward_prime_seq = process_good_seq(backward_good_seq)
        prime_seq = backward_prime_seq[2:][::-1] + forward_prime_seq
    unique_primes = sorted(set(prime_seq))
    letter_ordinals = [unique_primes.index(p) for p in prime_seq]
    return ''.join([chr(ord('A') + lo) for lo in letter_ordinals])


def process_good_seq(numbers: List[int]) -> List[int]:
    """extract primes from a sequence that does not start with 2 repeated numbers"""
    if len(numbers) < 2:
        raise ValueError('numbers must have at least length 2')
    if numbers[0] == numbers[1]:
        raise ValueError('the first 2 numbers must be different')
    prime_seq = []
    gcd01 = gcd(numbers[0], numbers[1])
    prime_seq.append(int(numbers[0] / gcd01))
    for n in numbers:
        prime_seq.append(int(n / prime_seq[-1]))
    return prime_seq


def gcd(a: int, b: int) -> int:
    """
    greatest common divisor

    >>> gcd(3, 1)
    1

    >>> gcd(35, 14)
    7

    >>> gcd(1, 3)
    1

    >>> gcd(14, 35)
    7
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
