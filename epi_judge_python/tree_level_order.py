import collections
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    elt_depth = collections.namedtuple('elt_depth', ['elt', 'depth'])
    queue = collections.deque()
    queue.append(elt_depth(tree, 0))
    acc = [[]]
    curr_depth = 0
    while len(queue) > 0:
        (elt, depth) = queue.popleft()
        if depth == curr_depth:
            acc[-1].append(elt.data)
        else:
            curr_depth += 1
            acc.append([elt.data])
        queue.extend([elt_depth(e, curr_depth + 1) for e in [elt.left, elt.right] if e])
    return acc


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    q = collections.deque()
    q_ = collections.deque()
    acc = []
    level_acc = []
    q.append(tree)

    while len(q) > 0:
        elt = q.popleft()
        level_acc.append(elt.data)
        q_.extend([e for e in [elt.left, elt.right] if e])
        if len(q) == 0:
            q, q_ = q_, q
            acc.append(level_acc)
            level_acc = []
    return acc


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    acc = []
    queue = [tree]
    while len(queue) > 0:
        acc.append([n.data for n in queue])
        queue = [c for n in queue for c in [n.left, n.right] if c]
    return acc


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
