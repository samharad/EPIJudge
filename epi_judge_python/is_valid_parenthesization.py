from test_framework import generic_test


PAREN_MATCH = {"{": "}",
               "[": "]",
               "(": ")"}


def is_well_formed(s: str) -> bool:
    stack = []
    for c in s:
        if c in PAREN_MATCH.keys():
            stack.append(c)
        elif len(stack) == 0 or c != PAREN_MATCH[stack.pop()]:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    generic_test.generic_test_main('is_valid_parenthesization.py',
                                   'is_valid_parenthesization.tsv',
                                   is_well_formed)
