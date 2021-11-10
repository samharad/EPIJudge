from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    e = L
    o = o_head = L.next
    while o and o.next:
        e.next = e = o.next
        o.next = o = e.next
    e.next = o_head
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
