import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    def xor(a, b):
        return a ^ b

    differing_bits = functools.reduce(xor, [*A, *range(len(A))])
    differ_bit = differing_bits & (~(differing_bits - 1))

    candidates = [i for i in A if i & differ_bit]
    candidates_ = [i for i in range(len(A)) if i & differ_bit]

    missing_or_dup = functools.reduce(xor, [*candidates, *candidates_])


    times_seen = 0
    for i in A:
        if i == missing_or_dup:
            times_seen += 1

    other = missing_or_dup ^ differing_bits
    duplicate, missing = (missing_or_dup, other) if times_seen == 2 else (other, missing_or_dup)

    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer)
