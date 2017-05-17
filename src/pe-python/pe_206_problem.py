#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  206-problem.py
# Created       :  Fri 08 May 2015 21:22:29
# Last Modified :  Fri 05 Jun 2015 07:20:53
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  CONCEALED SQUARE
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


import math
import time
import sys
from termcolor import colored
from random import randint as rnd


INIT_TIME = time.time()


def perf():
    """ Return  the performance time. """
    print("Performance time: %s" % (time.time() - INIT_TIME))


def error():
    # massage if not supported entering
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def rndset(num):
    ''' Return random sequence with defined part of it. '''
    seed = 2
    seq = ["1"]
    for s in xrange(0, num-1):
        if seed > 9:
            seed = 0
        seq.append(str(rnd(0, 9)))
        seq.append(str(seed))
        seed += 1
    return int("".join(seq))

def match(num):
    ''' Return True if seq is 1_2_3_4_..._n_... '''
    s = str(num)
    return not all(int(s[x*2]) == x+1 for x in range(9))


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    how_long = int(sys.argv[1])
    # while True:
    #     zuko = rndset(how_long)
    #     if int(math.sqrt(zuko))**2 == zuko:
    #         print "Got it", zuko
    #         break
    #     print math.sqrt(zuko), zuko
    n = 138902663
    # sqrt(19293949596979899)
    while match(n*n):
        n -= 2

    print n*10

    perf()


if __name__ == '__main__':
    main()
