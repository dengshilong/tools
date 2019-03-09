# coding:utf-8
from math import sqrt


def pone(p, u):
    c = 0
    for x in range(2, int(sqrt(p)) + 1):
        if p % x == 0 and x + int(p / x) < u:
            c += 1
    return c >= 2


def sone(s, u):
    for x in range(2, int(s / 2)):
        y = s - x
        if not pone(x * y, u):
            return False
    return True


def ptwo(p, u):
    c = 0
    for x in range(2, int(sqrt(p)) + 1):
        if p % x == 0 and x + int(p / x) < u:
            y = int(p / x)
            if sone(x + y, u):
                c += 1
    return c == 1


def stwo(s, u):
    c = 0
    for x in range(2, int(s / 2)):
        y = s - x
        if ptwo(x * y, u):
            c += 1
    return c == 1


if __name__ == "__main__":
    u = 100
    for x in range(2, int(u / 2)):
        for y in range(x + 1, u - x):
            p = x * y
            s = x + y
            if pone(p, u) and sone(s, u) and ptwo(p, u) and stwo(s, u):
                print("x: %d, y: %d, p: %d, s: %d " % (x, y, p, s))
