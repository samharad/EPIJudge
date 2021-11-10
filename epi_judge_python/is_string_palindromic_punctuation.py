from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    b = 0
    e = len(s) - 1
    while b < e:
        if not s[b].isalnum():
            b += 1
        elif not s[e].isalnum():
            e -= 1
        elif s[b].lower() != s[e].lower():
            return False
        else:
            b += 1
            e -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
