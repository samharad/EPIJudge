from typing import Tuple, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_and_height(tree: BinaryTreeNode) -> Optional[Tuple[bool, int]]:
    if not tree:
        return True, -1
    (l_bal, l_h) = is_balanced_and_height(tree.left)
    (r_bal, r_h) = is_balanced_and_height(tree.right)
    return l_bal and r_bal and abs(l_h - r_h) <= 1, max(l_h, r_h) + 1


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    is_balanced, _ = is_balanced_and_height(tree)
    return is_balanced


if __name__ == '__main__':
    generic_test.generic_test_main('is_tree_balanced.py',
                                   'is_tree_balanced.tsv',
                                   is_balanced_binary_tree)
