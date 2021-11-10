from test_framework import generic_test


def to_decimal(s: str, b: int) -> int:
    if s[0] == "-":
        return 0 - to_decimal(s[1:], b)
    if s[0] == "+":
        return to_decimal(s[1:], b)
    acc = 0
    for c in s:
        acc *= b
        acc += int(c, b)  # otherwise, map of char => int
    return acc


def to_base(n: int, b: int) -> str:
    if n < 0:
        return "-" + to_base(-n, b)
    if n == 0:
        return "0"
    acc = ""
    while n:
        acc += format(n % b, 'X')  # otherwise, map of dig => char
        n //= b
    return acc[::-1]


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    return to_base(to_decimal(num_as_string, b1), b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
