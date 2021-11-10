import functools

from test_framework import generic_test


def say(n: str):
    acc = (0, n[0], "")

    def reducer(acc, c):
        (count, letter, word) = acc
        if letter == c:
            count += 1
        else:
            word += str(count)
            word += letter
            count = 1
            letter = c
        return count, letter, word

    acc = functools.reduce(reducer, n, acc)
    (count, letter, word) = acc
    word += str(count)
    word += letter
    return word


def look_and_say(n: int) -> str:
    res = "1"
    for _ in range(n - 1):
        res = say(res)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
