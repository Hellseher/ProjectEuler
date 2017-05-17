#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  78-problem.py
# Created       :  Sat 18 Apr 2015 18:33:04
# Last Modified :  Sat 16 May 2015 16:55:39
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  COIN PARTIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can be separated into piles in
# exactly seven different ways, so p(5)=7.
#
# OOOOO
# OOOO O
# OOO OO
# OOO O O
# OO OO O
# OO O O O
# O O O O O
# Find the least value of n for which p(n) is divisible by one million.
# <END  OF  DESCRIPTION>-------------------------------------------------------


import time
import sys
from termcolor import colored


INIT_TIME = time.time()
table = []


def perf():
    millis = round((time.time() - INIT_TIME) * 1000)
    return "Perfomance time: %sms" % millis


def partitions(sum_, number):
    if number == 0:
        return 0
    elif sum_ == 0:
        return 1
    elif sum_ < 0:
        return 0
    return partitions(sum_, number - 1) + partitions(sum_ - number, number)


def partition(num):
    a = [0 for i in range(num + 1)]
    k = 1
    y = num - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def part_table(number):
    for i in xrange(1, number):
        for j in xrange(1, number):
            if i - j < 0:
                table[i][j] = table[i][j-1]
            table[i][j] = table[i][j-1] + table[i-j][j]
    return table[number][number]


def error():
    """ Massage if error entering """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():

    if len(sys.argv) != 2:
        error()

    number = int(sys.argv[1])

    print list(partition(number))
    print perf()


if __name__ == '__main__':
    main()


# -=:[ Alike problems ]:=-
# 31p
# -=:[ References ]:=-
# [1] : Partition (Number Theory),
# [2] : Euler' generation functions
# [3] : Hinderbur C. F. algorithm 1778
# [4] : Ehrlich algorithm
# [5] : Young A., Ferrers M. N.  diagrams
# [6] : Srinivasa Ramanujan
# [7] : Ferrers diagrams

# -=:[ Links ]:=-
# [ 1 ] : http://www.programminglogic.com/integer-partition-algorithm/
# [ 2 ] : http://arxiv.org/pdf/0909.2331v2.pdf
