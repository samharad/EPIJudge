import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if len(A) == 0:
        return 0

    i = j = 0
    total = 1
    while j < len(A):
        while j < len(A) and A[i] == A[j]:
            j += 1
        if j < len(A):
            i += 1
            A[i] = A[j]
            total += 1
    return total


# Per book, slightly more elegant
def delete_duplicates(A: List[int]) -> int:
    if len(A) == 0:
        return 0

    i = 0
    for x in A:
        if x != A[i]:
            i += 1
            A[i] = x
    return i + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
