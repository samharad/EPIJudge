from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    array = list(stream)
    acc = 0
    for i in range(2, 0, -1):
        counts = [0] * 2**16
        for x in array:
            if x >= acc:
                interesting_bits = (x >> (i * 16)) & (acc + 0xFFFF)
                counts[interesting_bits] += 1
        least_common, _ = sorted(enumerate(counts), key=lambda i_c: i_c[1])[0]
        acc += (least_common << i * 16)
    return acc


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
