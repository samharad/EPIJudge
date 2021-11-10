from test_framework import generic_test

CACHED = [int("{0:b}".format(x).zfill(16)[::-1], 2) for x in range(pow(2, 16))]


def reverse_bits(x: int) -> int:
    mask = 0xFFFF
    return (CACHED[(x & mask)] << 48) + \
           (CACHED[(x >> 16) & mask] << 32) + \
           (CACHED[(x >> 32) & mask] << 16) + \
           (CACHED[(x >> 48)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
