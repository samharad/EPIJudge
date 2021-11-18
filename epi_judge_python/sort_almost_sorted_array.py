import heapq
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = acc = []
    for i, x in enumerate(sequence):
        heapq.heappush(heap, x)
        if i >= k:
            acc.append(heapq.heappop(heap))
    while len(heap) > 0:
        acc.append(heapq.heappop(heap))
    return acc


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    generic_test.generic_test_main(
        'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
        sort_approximately_sorted_array_wrapper)
