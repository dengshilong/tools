import re
import reprlib
RE_WORD = re.compile('\w+') 

class Sentence:
    """
    >>> s = Sentence('word come here again')
    >>> for word in s:
    ...     print(word)
    ...
    word
    come
    here
    again
    >>> s = Sentence('word come here again')
    >>> it = iter(s) #
    >>> while True:
    ...     try:
    ...         print(next(it))
    ...     except StopIteration:
    ...         del it
    ...         break
    ...
    word
    come
    here
    again
    """
    def __init__(self, text): 
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
