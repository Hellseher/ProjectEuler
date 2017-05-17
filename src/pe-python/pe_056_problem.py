#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  problem-56.py
# Created       :  Wed 01 Apr 2015 18:36:51
# Last Modified :  Sun 19 Apr 2015 14:47:25
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  POWERFUL DIGIT SUM
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a**b, where a, b < 100, what is the
# maximum digital sum?


import sys
from termcolor import colored
import time


def digitsum(n):
    """ Digit sum of number n. """

    sys.setrecursionlimit(100000000)
    if n < 9:
        return n
    else:
        return (n % 10) + digitsum(n//10)

INITIATE_TIME = time.time()


def dict_print(D):
    """ Print out the dictionary D. """

    for key in D:
        print key, " -- ", D[key]


def power(*arg):
    """ Return n powered in n power """

    n = arg[0]
    if len(arg) > 1:
        d = arg[1]
    d_sum = []
    dict_sum = {}
    for i in xrange(n/2, n):
        for j in xrange(n/2, n):
            if digitsum(i**j) not in d_sum:
                d_sum.append(digitsum(i**j))
                key = str(i)+"^"+str(j)
                dict_sum[key] = digitsum(i**j)
    if 'd' in locals():
        return dict_print(dict_sum)
    return max(d_sum)


def error_argv():
    """ Massage if error entering """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():
    if len(sys.argv) != 2:
        error_argv()

    n = int(sys.argv[1])
    print power(n, "d")


if __name__ == "__main__":
    main()
    print ("exec time: %s" % (time.time() - INITIATE_TIME))
