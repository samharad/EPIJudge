from test_framework import generic_test


def calc_parity(x: int) -> int:
    par = 0
    while x:
        x = x & (x - 1)
        par ^= 1
    return par


CACHED_PARITIES = [calc_parity(i) for i in range(pow(2, 16))]


def parity(x: int) -> int:
    mask = 0xFFFF
    return CACHED_PARITIES[x >> 48] ^ \
        CACHED_PARITIES[(x >> 32) & mask] ^ \
        CACHED_PARITIES[(x >> 16) & mask] ^ \
        CACHED_PARITIES[x & mask]


def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
