from test_framework import generic_test


# Runtime: O(log(y))
# Actually book calculates big-O in terms of *bits* -- so,
# O(n), n being the number of bits used to represent y
def power(x: float, y: int) -> float:
    if x == 0:
        return 0
    if y == 1:
        return x
    if y == -1:
        return 1 / x
    if y == 0:
        return 1

    y_over_2 = y // 2

    a = power(x, y_over_2)
    b = a * a

    return b * power(x, int(y - (2 * y_over_2)))


# Solution improvements:
#   - Use bit tricks
#   - Get rid of special cases
#   - Use iteration to avoid function call overhead (not intuitive!)
def power(x: float, y: int) -> float:
    if y < 0:
        return 1 / power(x, -y)
    exp = y
    result = 1
    x_ = x
    while exp:
        if exp & 0x1:
            result *= x_
        x_ = x_ * x_
        exp >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
