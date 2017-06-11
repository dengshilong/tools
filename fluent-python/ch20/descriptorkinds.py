### auxiliary functions for display only ###
def cls_name(obj_or_cls): 
    cls = type(obj_or_cls) 
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj): 
    cls = type(obj) 
    if cls is type:
        return '<class {}>'.format(obj.__name__) 
    elif cls in [type(None), int]:
        return repr(obj) 
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

### essential classes for this example ###
class Overriding:
    """a.k.a. data descriptor or enforced descriptor"""
    def __get__(self, instance, owner): 
        print_args('get', self, instance, owner)

    def __set__(self, instance, value): 
        print_args('set', self, instance, value)

class OverridingNoGet:
    """an overriding descriptor without ``__get__``"""
    def __set__(self, instance, value): 
        print_args('set', self, instance, value)

class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""
    def __get__(self, instance, owner): 
        print_args('get', self, instance, owner)

class Managed:
    """
    >>> obj = Managed()
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> Managed.over
    -> Overriding.__get__(<Overriding object>, None, <class Managed>)
    >>> obj.over = 7
    -> Overriding.__set__(<Overriding object>, <Managed object>, 7)
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> obj.__dict__['over'] = 8
    >>> vars(obj)
    {'over': 8}
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> obj.over_no_get #doctest: +ELLIPSIS
    <__main__.OverridingNoGet object at 0x...>
    >>> Managed.over_no_get #doctest: +ELLIPSIS
    <__main__.OverridingNoGet object at 0x...>
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get #doctest: +ELLIPSIS
    <__main__.OverridingNoGet object at 0x...>
    >>> obj.__dict__['over_no_get'] = 9
    >>> obj.over_no_get
    9
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get
    9
    >>> obj = Managed()
    >>> obj.non_over
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>) 
    >>> obj.non_over = 7
    >>> obj.non_over
    7
    >>> Managed.non_over
    -> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
    >>> del obj.non_over
    >>> obj.non_over
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
    """
    over = Overriding() 
    over_no_get = OverridingNoGet() 
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
