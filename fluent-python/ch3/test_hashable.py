class UnHashable(object):
    """
    >>> a = UnHashable(3)
    >>> b = UnHashable(3)
    >>> a == b
    True
    """
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        import random
        return hash("{} {}".format(self.x, random.random()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
