import random
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def pivot_A(l, u, x) -> int:
        while l < u:
            while A[l] < x:
                l += 1
            while A[u] > x:
                u -= 1
            A[l], A[u] = A[u], A[l]
        return l

    i = pivot_A(0, len(A) - 1, A[random.randint(0, len(A) - 1)])
    while len(A) - i != k:
        if len(A) - i > k:
            i = pivot_A(i + 1, len(A) - 1, A[random.randint(i + 1, len(A) - 1)])
        else:
            i = pivot_A(0, i - 1, A[random.randint(0, i - 1)])
    return A[i]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
