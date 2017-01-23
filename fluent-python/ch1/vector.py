# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time    : 17/1/2 下午3:51
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com
# pylint: disable=C0103,R0903,C0111
from math import hypot


class Vector:
    """
    >>> v = Vector(0, 0)
    >>> v
    Vector(0, 0)
    >>> abs(v)
    0.0
    >>> bool(v)
    False
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # def __bool__(self):
        # return bool(abs(self))
        # return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    d = {}
    d.get()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
