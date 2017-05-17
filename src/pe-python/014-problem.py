#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  14-problem.py
# Created       :  Mon 27 Apr 2015 22:59:10
# Last Modified :  Sat 29 Aug 2015 23:33:00
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LONGEST COLLATZ SEQUENCE
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# The following iterative sequence is defined for the set
# of positive integers:
#
# n → n/2 (n is even) n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this
# sequence (starting at 13 and finishing at 1) contains 10 terms. Although
# it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    # show the performance time
    millis = int(time.time() - INIT_TIME)
    print("Performance time: %sms" % millis)


def error():
    # massage if not supported entering
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def collatz_seq_gen(n, iters):
    coll = n
    while coll != 1:
        if coll % 2 == 0:
            coll /= 2
            yield coll
        else:
            coll = coll*3 + 1
            yield coll
    # TODO some optimization with cache


cache = {1: 1}


def collat_cache(n):
    global cache
    if n not in cache:
        if n % 2 == 0:
            cache[n] = collat_cache(n/2) + 1
        else:
            cache[n] = collat_cache(3*n + 1) + 1
        return cache[n]


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    take_num = int(sys.argv[1])
    print collat_cache(take_num)
    # longest = 1
    # for i in xrange(take_num, take_num / 2, -1):
    #     if len(list(collatz_seq_gen(longest)))
    # < len(list(collatz_seq_gen(i))):
    #         longest = i
    # print longest
    perf()


if __name__ == '__main__':
    main()
