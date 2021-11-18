from typing import List

from test_framework import generic_test


def binary_search(A: List[int], k: int, l=None, u=None) -> int:
    l, u = l or 0, u if u is not None else len(A) - 1
    if l > u:
        return -1
    while l <= u:
        m = l + (u - l) // 2
        if A[m] == k:
            return m
        if A[m] < k:
            l = m + 1
        else:
            u = m - 1
    return -1


# I think this is O(logn)
def search_first_of_k(A: List[int], k: int) -> int:
    i = binary_search(A, k)
    last_i = i
    while i != -1:
        last_i = i
        i = binary_search(A, k, 0, i - 1)
    return last_i


# After glimpsing the book solution; equivalent solution,
# slightly more terse
def search_first_of_k(A: List[int], k: int) -> int:
    if len(A) == 0:
        return -1
    l, u = 0, len(A) - 1
    while l < u:
        m = l + (u - l) // 2
        if A[m] == k:
            u = m
        elif A[m] < k:
            l = m + 1
        else:
            u = m - 1
    return l if A[l] == k else -1


if __name__ == '__main__':
    generic_test.generic_test_main('search_first_key.py',
                                   'search_first_key.tsv',
                                   search_first_of_k)
