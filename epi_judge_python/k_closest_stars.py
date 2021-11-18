import functools
import heapq
import itertools
import math
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


class StarWrapper:
    star: Star

    def __init__(self, star: Star):
        self.star = star

    def __lt__(self, other):
        return self.star.distance > other.star.distance


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    def unwrap(wrappers: List[StarWrapper]) -> List[Star]:
        return [w.star for w in wrappers]
    elt = next(stars, None)
    heap = []
    for _ in range(k):
        if not elt:
            return unwrap(heap)
        heap.append(StarWrapper(elt))
        elt = next(stars, None)
    heapq.heapify(heap)

    while elt:
        heapq.heappushpop(heap, StarWrapper(elt))
        elt = next(stars, None)
    return unwrap(heap)


find_closest_k_stars(iter([Star(1, 1, 1), Star(0, 0, 0)]), 1)


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    generic_test.generic_test_main('k_closest_stars.py',
                                   'k_closest_stars.tsv',
                                   find_closest_k_stars_wrapper, comp)
