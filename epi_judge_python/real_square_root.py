import math

from test_framework import generic_test


def square_root(x: float) -> float:
    # If disallowed, use the binary search method from prev. problem
    # l = math.floor(math.sqrt(x))
    # u = l + 1
    l, u = (0, 1) if x < 1 else (1, x)
    while not math.isclose(x, l**2):
        m = l + ((u - l) / 2)
        if m**2 > x:
            u = m
        else:
            l = m
    return l


if __name__ == '__main__':
    generic_test.generic_test_main('real_square_root.py',
                                   'real_square_root.tsv', square_root)
