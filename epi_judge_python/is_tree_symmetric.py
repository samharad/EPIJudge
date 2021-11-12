from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def are_symmetric(a: BinaryTreeNode, b: BinaryTreeNode) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.data == b.data and are_symmetric(a.left, b.right) and are_symmetric(a.right, b.left)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return not tree or are_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    generic_test.generic_test_main('is_tree_symmetric.py',
                                   'is_tree_symmetric.tsv', is_symmetric)
