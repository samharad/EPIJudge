from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    overflow = True
    res = A
    while overflow and i >= 0:
        n = res[i]
        res[i] = (res[i] + 1) % 10
        overflow = n == 9
        i -= 1
    if overflow:
        # Per book: slick way to "prepend 1":
        res[0] = 1
        res.append(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
