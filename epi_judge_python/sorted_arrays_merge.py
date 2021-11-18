import collections
import heapq
from dataclasses import dataclass, field
from typing import List

from test_framework import generic_test


@dataclass(order=True)
class Entry:
    l: int = field(compare=False)
    idx: int = field(compare=False)
    elt: int


# O(nlog(k)) time, n being the total elts, k being num sequences; O(n) space (for the return value)
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [Entry(i, 0, l[0]) for i, l in enumerate(sorted_arrays)]
    heapq.heapify(heap)

    acc = []
    while len(heap) > 0:
        entry = heapq.heappop(heap)
        l, idx, elt = entry.l, entry.idx, entry.elt
        acc.append(elt)
        new_idx = idx + 1
        if len(sorted_arrays[l]) > new_idx:
            heapq.heappush(heap, Entry(l, new_idx, sorted_arrays[l][new_idx]))

    return acc


if __name__ == '__main__':
    generic_test.generic_test_main('sorted_arrays_merge.py',
                                   'sorted_arrays_merge.tsv',
                                   merge_sorted_arrays)
