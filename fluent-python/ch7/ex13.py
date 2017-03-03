def make_averager(): 
    """
    >>> avg = make_averager()
    >>> avg(10)
    Traceback (most recent call last):
    ...
    UnboundLocalError: local variable 'count' referenced before assignment
    >>>
    """
    count = 0
    total = 0
    def averager(new_value): 
        count += 1
        total += new_value 
        return total / count
    return averager

if __name__ == "__main__":
    import doctest
    doctest.testmod()
