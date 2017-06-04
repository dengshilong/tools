import doctest
class Class: 
    """
    >>> obj = Class()
    >>> vars(obj) #
    {}
    >>> obj.data #
    'the class data attr'
    >>> obj.data = 'bar' #
    >>> vars(obj) #
    {'data': 'bar'}
    >>> obj.data #
    'bar'
    >>> Class.data #
    'the class data attr'
    >>> Class.prop #
    <property object at 0x1072b7408> 
    >>> obj.prop #
    'the prop value'
    >>> obj.prop = 'foo' #
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute 
    >>> obj.__dict__['prop'] = 'foo' # 
    >>> vars(obj) #
    {'prop': 'foo', 'data': 'bar'}
    >>> obj.prop #
    'the prop value'
    >>> Class.prop = 'baz' # 
    >>> obj.prop #
    'foo'
    >>> obj.data #
    'bar'
    >>> Class.data #
    'the class data attr'
    >>> Class.data = property(lambda self: 'the "data" prop value') # 
    >>> obj.data #
    'the "data" prop value'
    >>> del Class.data # 
    >>> obj.data # 
    'bar'
    """

    data = 'the class data attr' 

    @property
    def prop(self):
        return 'the prop value'


if __name__ == "__main__":
    doctest.testmod()
