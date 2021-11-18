from test_framework import generic_test


def square_root(k: int) -> int:
    l, u, result = 0, k // 2 + 1, 0
    while l <= u:
        m = l + (u - l) // 2
        if m ** 2 <= k:
            result = m
            l = m + 1
        else:
            u = m - 1
    return result


if __name__ == '__main__':
    generic_test.generic_test_main('int_square_root.py',
                                   'int_square_root.tsv', square_root)
