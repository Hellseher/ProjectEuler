#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  09-problem.py
# Created       :  Mon 06 Apr 2015 15:04:57
# Last Modified :  Wed 25 Nov 2015 23:12:41
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  SPECIAL PYTHAGOREAN TRIPLET
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for wich,
#
#     a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


from termcolor import colored
from fractions import gcd
from math import sqrt
import platform
import time
import sys


INIT_TIME = time.time()


def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False


def pythanumber(s):
    for a in xrange(3, (s-3) / 3):
        for b in xrange(a+1, (s - 1 - a) / 2):
            c = s-a-b
            if pythagorean_triple(a, b, c):
                print ("a: %s, b: %s, c: %s, a*b*c: %s" % (a, b, c, a*b*c))
                print("Performance time: %s" % perf())
                quit()


def error():
    """ Massage if error """

    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def perf():
    # Return performance time of the program
    return ("Performance time: %s" % (time.time() - INIT_TIME))


def mnabc(num):
    # takes range of search, returns all possible Pythagorean triplets
    s2 = num / 2
    m_limit = int(sqrt(num * 2)) - 1
    for m in xrange(2, m_limit):
        if s2 % m == 0:
            sm = s2 / m
            while sm % 2 == 0:
                sm = sm / 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 / (k * m)
                    n = k - m
                    a = d * (m*m - n*n)
                    b = 2*d*m*n
                    c = d * (m*m + n*n)
                    print a, b, c, "\n"
                k += 2


def main():

    if len(sys.argv) != 2:
        error()

    s = int(sys.argv[1])

    print ("Platform: %s" % platform.platform())
    print ("Python build: %s %s\n" % platform.python_build())
    mnabc(s)
    print perf()


if __name__ == '__main__':
    main()

# -=:[ Alternatives ]:=-
# 39-problem.py
