#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  203-problem.py
# Created       :  Fri 08 May 2015 22:22:44
# Last Modified :  Mon 28 Sep 2015 00:35:40
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  SQUAREFREE BINOMIAL COEFFICIENTS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
#      The binomial coefficients nCk can be arranged in triangular form,
#      Pascal's triangle, like this:
#
#     1
#     1  1
#     1  2  1
#     1  3  3  1
#     1  4  6  4  1
#     1  5  10 10 5  1
#     1  6  15 20 15 6  1
#     1  7  21 35 35 21 7  1
#     .........

#     It can be seen that the first eight rows of Pascal's triangle contain
#     twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.
#
#     A positive integer n is called squarefree if no square of a prime divides
#     n.  Of the twelve distinct numbers in the first eight rows of Pascal's
#     triangle, all except 4 and 20 are squarefree. The sum of the distinct
#     squarefree numbers in the first eight rows is 105.
#
#     Find the sum of the distinct squarefree numbers in the first 51 rows of
#     Pascal's triangle.
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys

import pe  # Project Euler library

INIT_TIME = time.time()


def perf():
    # show the performance time
    millis = float(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def error():
    # massage if not supported entering

    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def sqfree(num):
    """ Return True if there is no square divisor of number num. """
    for i in [2, 3, 5, 7]:
        if num % i**2 == 0:
            return False
    return True


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    get_row = int(sys.argv[1])
    # get Pascal row from user
    distinct = set()
    # futre set of distinct numbers of Pascal triangle.
    dist_sqfree = []
    # distinct squarefree list of numbers

    for r in xrange(0, get_row):
        # find all distinct number of Pascal triangle up to get_row.
        row = list(pe.pclrow(r))
        for p in row:
            distinct.add(p)

    for i in distinct:
        if sqfree(i) and i % 4 != 0:
            dist_sqfree.append(i)

    print dist_sqfree
    print sum(dist_sqfree)

    perf()


if __name__ == '__main__':
    main()
