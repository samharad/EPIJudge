import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# def bubble_out(pivot: int, A: List[int], i: int) -> None:
#     dir = 1 if A[i] > pivot else -1
#     while 0 <= i + dir < len(A) and A[i + dir] == pivot:
#         swap = A[i]
#         A[i] = A[i + dir]
#         A[i + dir] = swap
#         i += dir
#     return

def helper(pivot: int, A: List[int]):
    i = 0
    for j in range(len(A)):
        if A[j] <= pivot:
            swap = A[j]
            A[j] = A[i]
            A[i] = swap
            i += 1
    return i


def dutch_flag_partition(pivot_index: int, A: List[int]) -> List[int]:
    pivot = A[pivot_index]
    helper(pivot, A)
    helper(pivot - 1, A)
    return A


def test_dutch_flag_partition():
    assert dutch_flag_partition(0, [1, 2, 3, 1]) == [1, 1, 2, 3]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
