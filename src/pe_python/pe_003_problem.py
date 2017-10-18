#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  problem-03.py
# Created       :  Mon 30 Mar 2015 19:06:41
# Last Modified :  Sat 14 Nov 2015 21:47:02
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LARGEST PRIME FACTOR
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# the prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


import sys
from math import sqrt
from termcolor import colored

import ProjectEuler as pe


def isprime(n):
    """ Check numer n i Prime """

    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def error(arg_list):
    """ Massage if error entering """

    if len(arg_list) != 2:
        print colored("..::Incorect amount of arguments::..", 'red')
        print colored("\tEnter just one integer", 'blue')
        quit()


def main():
    error(sys.argv)

    n = int(sys.argv[1])
    for largest_prime_factor in factors(n):
        if isprime(largest_prime_factor):
            print largest_prime_factor
    print pe.factors(n)


if __name__ == "__main__":
    main()
