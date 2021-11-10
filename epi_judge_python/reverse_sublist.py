from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == finish:
        return L

    dummy_head = pre = ListNode(next=L)
    ind = 0
    while ind < start - 1:
        pre = pre.next
        ind += 1
    i = pre
    j = i.next
    k = j.next
    num_reversed = 0
    while num_reversed < finish - start:
        i = j
        j = k
        k = k.next
        j.next = i
        num_reversed += 1
    pre.next.next = k
    pre.next = j
    return dummy_head.next


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = pre = ListNode(next=L)
    for _ in range(start - 1):
        pre = pre.next

    sublist_tail = pre.next
    for _ in range(finish - start):
        temp = sublist_tail.next
        temp.next, pre.next, sublist_tail.next = pre.next, temp, temp.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))