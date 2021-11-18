from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    s, l = sorted([0, len(A) - 1], key=lambda i: A[i])
    while (l + 1) % len(A) != s:
        m = min(s, l) + (abs(s - l) // 2)
        if A[m] <= A[s]:
            s = m
        else:
            l = m
    return s


if __name__ == '__main__':
    generic_test.generic_test_main('search_shifted_sorted_array.py',
                                   'search_shifted_sorted_array.tsv',
                                   search_smallest)
