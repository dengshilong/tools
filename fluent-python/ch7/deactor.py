# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time    : 17/2/7 下午2:52
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com

import functools


def log(arg):
    def dec(func, txt='call'):
        @functools.wraps(func)
        def wrp(*args, **kw):
            print('%s %s():' % (txt, func.__name__))
            return func(*args, **kw)
        return wrp
    if callable(arg):
        return dec(arg)
    else:
        return lambda f: dec(f, arg)


@log
def whoru():
    print('i am who i am')
whoru()


@log('EXEC')
def whoru():
    print('i am who i am')
whoru()
