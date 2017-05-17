#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  23-problem.py
# Created       :  Thu 11 Jun 2015 06:29:13
# Last Modified :  Sun 15 Nov 2015 00:07:46
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  NON-ABUNDANT SUMS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=23
#
# -=:[ Description ]:=-
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time

import ProjectEuler as pe


INIT_TIME = time.time()
ABUNDANTS = [x for x in range(1, 28123 + 1) if pe.is_abundant(x)]
# increase performance ime
abundants_set = set(ABUNDANTS)


def perf():
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    return "--------------------------------\n" \
        "Performance time: %s" % millis


def error():
    ''' Massage if not supported entering '''
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()



def is_abundant_sum(n):
    for i in ABUNDANTS:
        if i > n:
            return False
        if (n - i) in abundants_set:
            return True
    return False


def main():
    not_abundants_sum = 0
    for i in range(1, 28123+1):
        if not is_abundant_sum(i):
            not_abundants_sum += i

    print not_abundants_sum
    print perf()

if __name__ == '__main__':
    main()

# -=:[ Reference ]:=-
# [1] Perfect numbers
# [2] deficient numbers
# [3] Abundant number
