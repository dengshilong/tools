class Fibonacci:
    def __iter__(self):
        return FibonacciGenerator() 

class FibonacciGenerator:
    def __init__(self): 
        self.a = 0
        self.b = 1

    def __next__(self): 
        result = self.a
        self.a, self.b = self.b, self.a + self.b 
        return result

    def __iter__(self): 
        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()
