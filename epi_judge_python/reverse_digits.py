import collections
import functools

from test_framework import generic_test


# O(n), n being number of digits in x
def reverse(x: int) -> int:
    if x < 0:
        return 0 - reverse(-x)
    x_ = x
    acc = 0
    while x_:
        acc *= 10
        acc += (x_ % 10)
        x_ //= 10
    return acc


# O(number of digits in x)
# def reverse(x: int) -> int:
#     if x == 0:
#         return x
#     if x < 0:
#         return 0 - reverse(-x)
#
#     big = 0
#     while pow(10, big + 1) <= x:
#         big += 1
#
#     small = 0
#     acc = x
#
#     while small < big:
#         small_dig = (acc // pow(10, small)) % 10
#         big_dig = (acc // pow(10, big)) % 10
#
#         acc += ((small_dig - big_dig) * pow(10, big))
#         acc += ((big_dig - small_dig) * pow(10, small))
#
#         small += 1
#         big -= 1
#
#     return acc


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
