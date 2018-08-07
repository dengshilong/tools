def averager(): 
    """
    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
    """
    total = 0.0
    count = 0 
    average = None 
    while True:
        term = yield average 
        total += term
        count += 1
        average = total/count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
