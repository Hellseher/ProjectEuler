#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  27-problem.py
# Created       :  Fri 03 Apr 2015 21:19:21
# Last Modified :  Sun 19 Apr 2015 14:34:17
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  QUADRATIC PRIMES
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# Euler discovered the remarkable quadratic formula:
#     n**n + n + 41
# it turns out that the formula will produce 40 primes
# for the consecutive values
# 0 < n < 40. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41
# is divisible
# by 41, and certainly when n = 41.


from math import sqrt
from subprocess import call
from termcolor import colored
import time
import sys


INIT_TIME = time.time()
TERM_WIDTH = call(["tput", "cols"])


def isprime(number):
    """ Check primirity of number """

    if number == 0 or number == 1:
        return False
    for dev in xrange(2, int(sqrt(number)) + 1):
        if number % dev == 0:
            return False
    return True


def show_grid(L):
    """ Print out grid of given list """

    dim = int(sqrt(len(L)))  # grid W x H
    for item in L:
        print item
        if L.index(item) % dim == 0:
            print "\n"


def error():
    """ Massage if error """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just two integer", 'blue')
    quit()


def main():
    if len(sys.argv) != 3:
        error()

    a = sys.argv[1]
    b = sys.argv[2]

    n_wanted = 0
    for i in xrange(a * -1, a + 1):
        for j in xrange(b * -1, b + 1):
            n = 0
            while True:
                prime_check = abs(n**2 + i*n + j)
                if isprime(prime_check):
                    n += 1
                else:
                    if n > n_wanted:
                        n_wanted = n
                        A = i
                        B = j
                    break

    print A, B, n_wanted
    print ("Perfomence time: %s" % (time.time() - INIT_TIME))


if __name__ == "__main__":
    main()
