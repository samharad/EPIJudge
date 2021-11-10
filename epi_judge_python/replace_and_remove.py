import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    w = len(s) - 1
    r = size - 1
    count = size
    while r >= 0:
        if s[r] == "b":
            r -= 1
            count -= 1
        elif s[r] == "a":
            s[w] = s[w-1] = "d"
            r -= 1
            w -= 2
            count += 1
        else:
            s[w] = s[r]
            r -= 1
            w -= 1
    w = 0
    r = len(s) - count
    while w < count:
        s[w] = s[r]
        w += 1
        r += 1
    return count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
