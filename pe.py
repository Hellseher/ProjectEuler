#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  pe.py
# Created       :  Mon 27 Apr 2015 19:01:22
# Last Modified :  Sat 16 May 2015 12:32:01
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PROJECT EULERS FUNCTIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# This file contains functions which I used for solving Project Euler's
# problems.
# <END  OF  DESCRIPTION>-------------------------------------------------------


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

# -=:[ Figurate numbers ]:=----------------------------------------------------

def triangn(num):
    """ Yield a list of ingeter triangular number up to num. """
    for tr in xrange(0, num):
        yield tr*(tr+1)/2
    # -=:[ Reference ]:=-
    # Carl Friedrich Gauss
    # OEIS : A000217
    # -=:[ Links ]:=-
    # https://en.wikipedia.org/wiki/Triangular_number
