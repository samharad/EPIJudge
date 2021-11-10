import math
from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    candidates = [False, False] + [True] * (n - 1)
    primes = []
    for x in range(2, n + 1):
        if candidates[x]:
            primes.append(x)
            for i in range(x * 2, n + 1, x):
                candidates[i] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
