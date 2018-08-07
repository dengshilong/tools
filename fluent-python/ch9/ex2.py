from array import array
import math 


class Vector2d:
    """
    >>> v1 = Vector2d(3, 4) 
    >>> print(v1.x, v1.y) 
    3.0 4.0
    >>> x,y=v1
    >>> x,y
    (3.0, 4.0)
    >>> v1
    Vector2d(3.0, 4.0)
    >>> v1_clone = eval(repr(v1)) 
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets 
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector2d(0, 0))
    (True, False)
    """
    typecode = 'd'
    
    def __init__(self, x, y): 
        self.x = float(x) 
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))) 

    def __eq__(self, other):
        return tuple(self) == tuple(other) 

    def __abs__(self):
        return math.hypot(self.x, self.y) 

    def __bool__(self):
        return bool(abs(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
