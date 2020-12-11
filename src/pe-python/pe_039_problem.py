#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  39-problem.py
# Created       :  Wed 22 Apr 2015 18:23:20
# Last Modified :  Sat 29 Aug 2015 23:12:33
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  INTEGER RIGHT TRIANGLES
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=39
#
# -=:[ Description ]:=-
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
from collections import defaultdict
import time
import sys


INIT_TIME = time.time()


def perf():
    # show the perfomance time
    millis = int(time.time() - INIT_TIME)
    print("Perfomance time: %s" % millis)


def error():
    # massage if not supported entering
    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    pdic = defaultdict(int)
    tr_perimeter = int(sys.argv[1])
    for c in xrange(1, tr_perimeter):
        for a in xrange(1, tr_perimeter):
            for b in xrange(1, tr_perimeter):
                if c + a + b <= tr_perimeter:
                    if c**2 == a**2 + b**2:
                        if a+b+c in pdic:
                            pdic[a+b+c] += 1
                        else:
                            pdic[a+b+c] = 1
    for key in pdic:
        print(pdic[key], key)

    perf()


if __name__ == '__main__':
    main()

# -=:[  ]:=-
# 09-problem.py
