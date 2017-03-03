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
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
