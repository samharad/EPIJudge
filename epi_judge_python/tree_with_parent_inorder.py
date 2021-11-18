from enum import Enum
from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def walk_up_from_right(node: BinaryTreeNode) -> BinaryTreeNode:
    while node.parent and node.parent.right is node:
        node = node.parent
    return node


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []

    acc = []
    i = tree
    direction = Direction.LEFT

    while True:
        match direction:
            case Direction.LEFT:
                if i.left:
                    i = i.left
                else:
                    acc.append(i.data)
                    direction = Direction.RIGHT
            case Direction.RIGHT:
                if i.right:
                    i = i.right
                    direction = Direction.LEFT
                else:
                    direction = Direction.UP
            case Direction.UP:
                if not i.parent:
                    break
                if i is i.parent.left:
                    i = i.parent
                    acc.append(i.data)
                    direction = Direction.RIGHT
                else:
                    i = i.parent
    return acc


if __name__ == '__main__':
    generic_test.generic_test_main('tree_with_parent_inorder.py',
                                   'tree_with_parent_inorder.tsv',
                                   inorder_traversal)
