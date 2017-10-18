#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  31-problem.py
# Created       :  Wed 13 May 2015 23:32:02
# Last Modified :  Sun 27 Sep 2015 23:09:30
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  COIN SUMS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=31
#
# -=:[ Description ]:=-
# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#     How many different ways can £2 be made using any number of coins?
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys


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


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    target = int(sys.argv[1])  # get limit of calculs
    coints = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = 1

    for i in coints:
        for j in xrange(i, target):
            ways[j] += ways[j - i]

    print ways

    perf()


if __name__ == '__main__':
    main()

# -=:[ Alike problems ]:=-
# ,78p,
# -=:[ References ]:=-
