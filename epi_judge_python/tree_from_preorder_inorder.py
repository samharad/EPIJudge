import collections
from typing import List, Deque, Set, Optional, Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def partition_inorder(l: List[int], x: int) -> Tuple[List[int], List[int]]:
    i = l.index(x)
    return l[0:i] if i else [], l[i + 1:] if i < len(l) - 1 else []


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> Optional[BinaryTreeNode]:
    if len(preorder) == 0:
        return None
    elt = preorder[0]
    root = BinaryTreeNode(elt)

    left_ino, right_ino = partition_inorder(inorder, elt)
    left_pre, right_pre = preorder[1:len(left_ino)+1], preorder[len(left_ino)+1:]

    root.left = binary_tree_from_preorder_inorder(left_pre, left_ino)
    root.right = binary_tree_from_preorder_inorder(right_pre, right_ino)

    return root


if __name__ == '__main__':
    generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                   'tree_from_preorder_inorder.tsv',
                                   binary_tree_from_preorder_inorder)
