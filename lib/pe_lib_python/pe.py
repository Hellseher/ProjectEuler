#! /usr/bin/env python
# _*_ coding : UTF-8 _*_
# File       :  pe.py
# Created    :  Mon 27 Apr 2015 19:01:22
# Modified   :  <2017-8-15 Tue 22:28:37 BST> sharlatan
# Maintainer :  sharlatan, <sharlatanus@gmail.com>
# Title      :
# License    :  Same as Python (GPL)
# Credits    :


import math


def isp(num):
    """ Check num for primirity. """
    if num == 1:
        return False
    elif num < 4:
        return True  # 2 and 3 are primes
    elif num % 2 == 0:
        return False
    elif num < 9:  # already excluded 4, 6 and 8.
        return True
    elif num % 3 == 0:
        return False
    else:
        r = int(math.sqrt(num))  # rounded r so that r*r <= num
        f = 5
        while f <= r:
            if num % f == 0:
                return False
            elif num % (f + 2) == 0:
                return False
            f += 6
    return True


def ps(num):
    """ Yield prime sieve up to sqrt(num). """
    if num == 2:
        yield 2
    for i in xrange(1, num):
        if isp(i):
            yield i


def ds(num):
    """ Return digits sum of num. """
    if num < 10:
        return num
    return num % 10 + ds(num // 10)


def dfs(num):
    """ Return factorised digits sum of num. """
    if num < 10:
        return math.factorial(num)
    return math.factorial(num % 10) + dfs(num // 10)


def dsfs(num):
    """ Return digit sum of factorised digit sum. """
    return ds(dfs(num))


def pclrow(n):
    """ Yield the n'th row of Pascal triangle. """
    pos = 1
    yield pos
    for k in xrange(1, n):
        pos = pos * (n + 1 - k)/k
        yield pos
    yield 1


def trnum(num):
    """ Yield a list of triangle number up to num. """
    for tr in xrange(1, num):
        yield tr*(tr+1)/2
