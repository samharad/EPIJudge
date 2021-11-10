from typing import Optional, Tuple

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = leader = follower = ListNode(next=L)
    for _ in range(0, k):
        leader = leader.next
    while leader.next:
        leader = leader.next
        follower = follower.next
    follower.next = follower.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
