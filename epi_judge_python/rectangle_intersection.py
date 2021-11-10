import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    none_rect = Rect(0, 0, -1, -1)

    # TODO - you fill in here.
    rs = [r1, r2]
    rs.sort(key=lambda r: r.x)
    (a, b) = rs
    if b.x > a.x + a.width:
        return none_rect
    x = b.x
    w = min(a.x + a.width, b.x + b.width) - x

    rs.sort(key=lambda r: r.y)
    (a, b) = rs
    if b.y > a.y + a.height:
        return none_rect
    y = b.y
    h = min(a.y + a.height, b.y + b.height) - y
    return Rect(x, y, w, h)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
