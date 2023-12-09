"""
number.py:
    Implementations of algorithms used in discrete mathematics, combinatorics,
    and number theory.
"""


def extended_euclidean(a: int, b: int) -> tuple[int, int]:
    """
    Find (x, y) such that ax + by = gcd(a, b).
    """

    if a == 0:
        return 0, 1

    x, y = extended_euclidean(b % a, a)

    return y - (b // a) * x, x


def chinese_remainder_theorem(remainders: list[int], divisors: list[int]) -> int:
    """
    Find x such that x congruent a[i] % n[i] for all a[i] in remainders and
    n[i] in divisors.

    The returned x is the smallest positive x, but it's periodic with period
    prod(divisors).
    """

    assert len(remainders) == len(divisors)
    assert len(remainders) > 1

    x = 0
    n = 1
    for i in range(len(remainders)):
        a1, a2 = x, remainders[i]
        n1, n2 = n, divisors[i]
        m1, m2 = extended_euclidean(n1, n2)
        n = n1 * n2
        x = (a1 * m2 * n2 + a2 * m1 * n1) % n

    return x
