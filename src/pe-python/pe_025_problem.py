#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  25-problem.py
# Created       :  Wed 15 Apr 2015 23:45:59
# Last Modified :  Thu 16 Apr 2015 00:05:45
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  1000-DIGIT FIBONACCI NUMBER
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# .-=:[ Description ]:=-
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#   Hence the first 12 terms will be:
#
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
#  The 12th term, F12, is the first term to contain three digits.
#
#  What is the first term in the Fibonacci sequence to contain 1000 digits?


def fi(num):
    if num < 2:
        return num
    else:
        return fi(num - 1) + fi(num - 2)


from math import sqrt


def analytic_fibonacci(n):
    sqrt_5 = sqrt(5)
    p = (1 + sqrt_5) / 2
    q = 1/p
    return int((p**n + q**n) / sqrt_5 + 0.5)


def fibIter(n):
    if n < 2:
        return n
    fibPrev = 1
    fib = 1
    for num in xrange(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


def main():
    num = 12
    while len(str(fibIter(num))) < 1000:
        num += 1
    print fibIter(num)
    print num


if __name__ == '__main__':
    main()
