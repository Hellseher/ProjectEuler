#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  49-problem.py
# Created       :  Mon 11 May 2015 22:46:40
# Last Modified :  Tue 12 May 2015 00:41:26
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PRIME PERMUTATIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

#
# <END  OF  DESCRIPTION>-------------------------------------------------------

from termcolor import colored
import time
import sys


INIT_TIME = time.time()

with open('primes_digits_4', 'r') as f:
    # four digit prime
    fdp = map(int, f.read().splitlines())

def perf():
    # show the performance time
    millis = float(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def permut(*argv):
    """ Return False if any of arguments not equal. """
    first = sorted(argv[0])
    hl = len(argv)
    for i in xrange(0, hl):
        if first != sorted(argv[i]):
            return False
        else:
            first = sorted(argv[i])
    return True


def main():
    # let's begin
    # Look for primes in the primes list that are permutations of each other. By
    # defining c = (b - a) + b we are able to check for equal distant numbers.
    for a in fdp:
        for b in fdp:
            c = (b - a) + b
            if c > b > a and set(str(a)) == set(str(b)) == set(str(c)) and c in fdp:
                print "{0}{1}{2}" .format(a, b, c)
    perf()


if __name__ == '__main__':
    main()

# -=:[ Referance ]:=-
# [1] arithmetic progression
# [2] Prime numbers
# [3] Permutation
