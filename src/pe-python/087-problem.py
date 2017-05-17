#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  87-problem.py
# Created       :  Wed 29 Apr 2015 23:33:02
# Last Modified :  Wed 16 Sep 2015 23:07:49
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PRIME POWER TRIPLES
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=87
#
# -=:[ Description ]:=-
# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:
#
#     28 = 2^2 + 2^3 + 2^4
#     33 = 3^2 + 2^3 + 2^4
#     49 = 5^2 + 2^3 + 2^4
#     47 = 2^2 + 3^3 + 2^4
#
#     How many numbers below fifty million can be expressed as the sum of a
#     prime square, prime cube, and prime fourth power?
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys

import pe

INIT_TIME = time.time()
# with open("primes") as f:
#     PRIMES = map(int, f.read().splitlines())


def perf():
    # show the performance time
    millis = time.time() - INIT_TIME
    print("Performance time: %s" % millis)


def error():
    # massage if not supported entering

    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


# def count_lim(num):
#     """ Return count limit for prime power triples. """
#     global PRIMES
#     for p in PRIMES:
#         if p**2 + 2**3 + 2**4 >= num:
#             p_id = PRIMES.index(p)  # index of prime limit
#             return PRIMES[:p_id+1]
#

def main():
    if len(sys.argv) != 2:
        error()                     #  check error() to edit the massage

    """  let's begin """
    get_limit = int(sys.argv[1])
    p_list = list(pe.ps(get_limit)) #  generate a list of primes)
    power_triples = set()              #  list of posible triples

    for a in p_list:
        for b in p_list:
            ab = a**4 + b**3
            if ab >= get_limit:
                break
            for c in p_list:
                triples = c**2 + ab
                if triples >= get_limit:
                    break
                power_triples.add(triples)

    print len(power_triples)
    perf()


if __name__ == '__main__':
    main()
