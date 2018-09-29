# -*- coding: utf-8 -*-

import re
import time


if __name__ == '__main__':
    n = 30
    for i in range(1, n):
        start = time.time()
        s = 'a' * i + 'x'
        re.match('^(a+)+$', s)
        end = time.time()
        print(i, 'consume time: ', end - start)
