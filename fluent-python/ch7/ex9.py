def make_averager():
    """
    >>> avg = make_averager() 
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12) 
    11.0
    """
    series = []
    def averager(new_value): 
        series.append(new_value) 
        total = sum(series) 
        return total/len(series)
    return averager

if __name__ == "__main__":
    import doctest
    doctest.testmod()
