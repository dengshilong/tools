class Cheese(object):
    """
    >>> import weakref
    >>> stock = weakref.WeakValueDictionary()
    >>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    >>> for cheese in catalog:
    ...     stock[cheese.kind] = cheese
    ...
    >>> sorted(stock.keys())
    ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
    >>> del catalog
    >>> sorted(stock.keys())
    ['Parmesan']
    >>> del cheese
    >>> sorted(stock.keys())
    []
    """

    def __init__(self, kind):
        self.kind = kind 

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

if __name__ == "__main__":
    import doctest
    doctest.testmod()
