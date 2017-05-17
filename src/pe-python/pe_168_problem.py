#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  168-problem.py
# Created       :  Sat 02 May 2015 21:49:22
# Last Modified :  Thu 14 May 2015 00:13:11
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  NUMBER ROTATIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# Consider the number 142857. We can right-rotate this number by moving the last
# digit (7) to the front of it, giving us 714285.  It can be verified that
# 714285=5×142857.bit_lengthThis demonstrates an unusual property of 142857: it
# is a divisor of its right-rotation.
#
# Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have
# this property.
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


import sys
import math
import time

from termcolor import colored

import pe

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


def numrotor(num):
    """ Returns rotateded number and last digit of num. """
    dp = int(math.log10(num))
    last_digit = num % 10
    rotation = num//10 + last_digit * 10**dp
    if rotation == num * (rotation % 10):
        return True
    return False


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    get_num = int(sys.argv[1])

    # takes a loooot time to pass them all...
    step = 10
    while step < 10**get_num:
        if numrotor(step):
            print step, pe.ds(step)
        step += 1

    perf()


if __name__ == '__main__':
    main()
