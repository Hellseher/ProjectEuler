#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  51-problem.py
# Created       :  Mon 18 May 2015 23:04:51
# Last Modified :  Wed 16 Sep 2015 22:23:12
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993.  Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.
# <END  OF  DESCRIPTION>-------------------------------------------------------


import time


INIT_TIME = time.time()

with open("primes", 'r') as f:
    PRIMES = f.read().splitlines()


def perf():
    # show the performance time
    millis = float(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def longseq(num):
    """ Return found  digits sequence from num.  """
    num = str(num)
    first = num[0]
    sequence = 0
    for i in num:
        if first == i:
            print i, first
            if num.index(num)+1 >= num.index(i):
                first = i
                sequence += 1
            else:
                return first, sequence

def main():
        # check error() to edit the massage
    # let's begin
    for p in PRIMES:
        print "".join(set(p))

    perf()


if __name__ == '__main__':
    main()
