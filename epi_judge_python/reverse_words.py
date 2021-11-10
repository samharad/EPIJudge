import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse(s, i, j) -> None:
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return


def reverse_each_word(s: List[str]) -> None:
    i = j = 0

    def next_word(i: int) -> tuple[int, int]:
        while i < len(s) and not s[i].isalnum():
            i += 1
        j = i
        while j + 1 < len(s) and s[j + 1].isalnum():
            j += 1
        return i, j

    i, j = next_word(i)
    while i < len(s):
        reverse(s, i, j)
        i, j = next_word(j + 1)
    return


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    reverse(s, 0, len(s) - 1)
    reverse_each_word(s)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
