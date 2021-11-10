from typing import List

from test_framework import generic_test


def spiral(m: List[List[int]], offset: int) -> List[int]:
    b, e = offset, len(m) - offset
    if b == e:
        return []
    if b + 1 == e:
        return [m[b][e - 1]]
    acc = []
    # Top edge
    for i in range(b, e - 1):
        acc.append(m[b][i])
    # Right edge
    for i in range(b, e - 1):
        acc.append(m[i][e - 1])
    # Bottom edge
    for i in range(e - 1, b, -1):
        acc.append(m[e - 1][i])
    # Left edge
    for i in range(e - 1, b, -1):
        acc.append(m[i][b])
    return acc + spiral(m, offset + 1)


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    return spiral(square_matrix, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
