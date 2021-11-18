import heapq
from typing import Iterator, List

from test_framework import generic_test


# Runtime: O(nlog(n/2)); Space: O(n)
def online_median(sequence: Iterator[int]) -> List[float]:
    max_heap, min_heap = [], []

    acc = []
    for i, x in enumerate(sequence):
        if i == 0:
            heapq.heappush(max_heap, 0 - x)
            acc.append(x)
        elif not i % 2:
            # Even index, so heaps are balanced coming in, but lopsided after pushing
            a, b, c = sorted([(0 - heapq.heappop(max_heap)), heapq.heappop(min_heap), x])
            acc.append(b)
            heapq.heappush(max_heap, 0 - a)
            heapq.heappush(max_heap, 0 - b)
            heapq.heappush(min_heap, c)
        else:
            # Odd index, so heaps are lopsided coming in
            a, b = sorted([x, (0 - heapq.heappop(max_heap))])
            heapq.heappush(max_heap, 0 - a)
            heapq.heappush(min_heap, b)
            acc.append(((0 - max_heap[0]) + min_heap[0]) / 2)
    return acc


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                   online_median_wrapper)
