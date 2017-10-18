#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  511-problem.py
# Created       :  Sun 19 Apr 2015 14:14:39
# Last Modified :  Sun 19 Apr 2015 15:54:48
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  SEQUENCES WITH NICE DIVISIBILITY PROPERTIES
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
# Let Seq(n,k) be the number of positive-integer sequences
# {ai} 1≤i≤n of length n such that:
#
# n is divisible by ai for 1 ≤ i ≤ n, and
# n + a1 + a2 + ... + an is divisible by k.
# Examples:
#
#     Seq(3,4) = 4, and the 4 sequences are:
#         {1, 1, 3}
#         {1, 3, 1}
#         {3, 1, 1}
#         {3, 3, 3}
#
#     Seq(4,11) = 8, and the 8 sequences are:
#         {1, 1, 1, 4}
#         {1, 1, 4, 1}
#         {1, 4, 1, 1}
#         {4, 1, 1, 1}
#         {2, 2, 2, 1}
#         {2, 2, 1, 2}
#         {2, 1, 2, 2}
#         {1, 2, 2, 2}
#
# The last nine digits of Seq(1111,24) are 840643584.
# Find the last nine digits of Seq(1234567898765,4321).
# <END  OF  DESCRIPTION>-------------------------------------------------------


from math import sqrt
from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    """ return performance time of the program """

    return ("Performance time: %s" % (time.time() - INIT_TIME))


def error():
    """ Massage if error """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just two integer", 'blue')
    quit()


def divisors(num):
    """ takes a number, return valid quantity of its divisors """

    give_div_back = []
    give_div_back.append(1)
    if num == 1:
        return give_div_back
    elif num < 4:
        give_div_back.append(num)
        return give_div_back
    elif num % 2 == 0:
        if num % 3 == 0:
            give_div_back.append(3)
        elif num % 4 == 0:
            give_div_back.append(4)
        give_div_back.append(num)
        give_div_back.append(2)
    elif num < 9:
        give_div_back.append(num)
        return give_div_back
    elif num % 3 == 0:
        give_div_back.append(3)
    else:
        give_div_back.append(num)
        for i in xrange(5, int(sqrt(num))):
            if num % i == 0:
                give_div_back.append(i)
                give_div_back.append(num//i)
    give_div_back.sort()
    return give_div_back


def main():

    if len(sys.argv) != 3:
        error()
    num = int(sys.argv[1])
    kof = int(sys.argv[2])
    print num, kof
    print divisors(num)
    total_sum = sum(divisors(num)) + num
    if total_sum % 4321 == 0:
        print "yes!"
    else:
        print "no!!!!"

if __name__ == '__main__':
    main()
