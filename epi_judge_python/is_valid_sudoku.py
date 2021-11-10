import math
from typing import List

from test_framework import generic_test


def is_valid_sudoku_segment(l: List[int]) -> bool:
    committed = [x for x in l if x != 0]
    return len(committed) == len(set(committed))


def grab_box(m: List[List[int]], x_y: (int, int), size: int) -> List[int]:
    (x, y) = x_y
    inds = [(i, j) for i in range(size) for j in range(size)]
    return [m[x+i][y+j] for (i, j) in inds]


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    box_dim = int(math.sqrt(len(partial_assignment)))
    box_range = range(0, len(partial_assignment) - 1, box_dim)
    box_inds = [(i, j) for i in box_range for j in box_range]
    boxes = [grab_box(partial_assignment, (i, j), box_dim) for (i, j) in box_inds]
    # Rows
    return all(
        # Row
        [is_valid_sudoku_segment(l) for l in partial_assignment] + \
        # Col
        [is_valid_sudoku_segment(c) for c in zip(*partial_assignment)] + \
        # Box
        [is_valid_sudoku_segment(box) for box in boxes]
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
