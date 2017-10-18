#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          : 20-problem.py
# Created       : Wed 08 Apr 2015 20:22:58
# Last Modified : Sat 18 Apr 2015 22:22:33
# Maintainer    : sharlatan, <sharlatanus@gmail.com>
# Title         : FACTORIAL DIGIT SUM
# License       : Same as Python (GPL)
# Credits       : https://projecteuler.net/
#
# -=:[ Description ]:=-
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!s


import sys
import time


INIT_TIME = time.time()


def fac(num):
    """ takes num, returns factorial of it """

    if num == 1:
        return num
    return num * fac(num - 1)


def digit_sum(num):
    """ takes num, returns sum of its digits """

    if num < 10:
        return num
    return num % 10 + digit_sum(num // 10)


def error():
    print ("Wrong number of args")
    quit()


def perf():
    print ("Performance time: %s" % (time.time() - INIT_TIME))


def main():

    if len(sys.argv) != 2:
        error()

    num = int(sys.argv[1])
    print digit_sum(fac(num))

    print perf()


if __name__ == "__main__":
    main()
