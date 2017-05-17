#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          : 10-problem.py
# Created       : Wed 08 Apr 2015 20:40:07
# Last Modified : Sat 18 Apr 2015 18:30:21
# Maintainer    : sharlatan, <sharlatanus@gmail.com>
# Title         : SUMMATION OF PRIMES
# License       : Same as Python (GPL)
# Credits       : https://projecteuler.net
#
# -=:[ Description ]:=-
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


import sys
import time
from math import sqrt
from termcolor import colored


INIT_TIME = time.time()


def isprime(num):
    """ check if num is prime number, fast check """

    if num in (2, 3, 5):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in xrange(5, int(sqrt(num)), 6):
        if num % i == 0:
            return False
        elif num % (i + 2) == 0:
            return False
    return True


def error():

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def perf():
    print ("Performance time: %s" % (time.time() - INIT_TIME))


def main():

    if len(sys.argv) != 2:
        error()
    num = int(sys.argv[1])
    PRIME_SUM = 0
    PRIM_COUNT = 0

    for i in xrange(2, num + 1):
        if isprime(i):
            PRIME_SUM += i
            PRIM_COUNT += 1

    print PRIME_SUM
    print PRIM_COUNT

    print perf()


if __name__ == "__main__":
    main()
