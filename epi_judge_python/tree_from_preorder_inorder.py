import collections
from typing import List, Deque, Set

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def reconstruct(preorder: Deque[int], inorder: Deque[int], seen: Set[int]) -> BinaryTreeNode:
    i = inorder[0]
    p = preorder.popleft()

    n = BinaryTreeNode(p)
    seen.add(p)

    if i != p:
        n.left = reconstruct(preorder, inorder, seen)
    else:
        inorder.popleft()

    if i not in seen:
        n.right = reconstruct(preorder, inorder, seen)
    else:
        inorder.popleft()
    return n


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    res = reconstruct(collections.deque(preorder), collections.deque(inorder), set())
    print(res)
    return res


if __name__ == '__main__':
    generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                   'tree_from_preorder_inorder.tsv',
                                   binary_tree_from_preorder_inorder)
