import functools
from typing import Tuple

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def advance(l: ListNode) -> Tuple[int, ListNode]:
        length = 0
        last = None
        while l:
            length += 1
            last = l
            l = l.next
        return length, last

    def find_intersection(shortl, shortlen, longl, longlen):
        for _ in range(longlen - shortlen):
            longl = longl.next
        while shortl is not longl:
            shortl = shortl.next
            longl = longl.next
        return shortl

    len0, last0 = advance(l0)
    len1, last1 = advance(l1)

    if not last0 or not last1 or last0 is not last1:
        return None

    return find_intersection(l0, len0, l1, len1) if len0 < len1 else find_intersection(l1, len1, l0, len0)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
