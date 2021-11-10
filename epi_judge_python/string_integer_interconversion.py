from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x < 0:
        return "-" + int_to_string(-x)
    if x == 0:
        return "0"
    acc = ""
    while x:
        dig = x % 10
        acc += str(dig)
        x //= 10
    return acc[::-1]


def string_to_int(s: str) -> int:
    if s[0] == "+":
        return string_to_int(s[1:])
    if s[0] == "-":
        return 0 - string_to_int(s[1:])
    acc = 0
    for c in s:
        acc *= 10
        acc += int(c)
    return acc


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
