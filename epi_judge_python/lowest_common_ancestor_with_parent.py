import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def height(node: BinaryTreeNode) -> int:
    height = 0
    while node.parent:
        height += 1
        node = node.parent
    return height


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    h0, h1 = height(node0), height(node1)
    while h0 < h1:
        node1 = node1.parent
        h1 -= 1
    while h1 < h0:
        node0 = node0.parent
        h0 -= 1
    while node0 and node1 and node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0 if node0 is node1 else None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                   'lowest_common_ancestor.tsv',
                                   lca_wrapper)
