#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  test.py
# Created       :  Sat 02 May 2015 00:35:09
# Last Modified :  Wed 27 May 2015 21:43:16
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
#
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


import time
import sys

import ProjectEuler as pe

INIT_TIME = time.time()


def perf():
    # show the performance time
    millis = float(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def num_segment(n):
    mode = 0
    while n:
        if n & 1:
            if mode <= 0:
                mode = -mode + 1
        else:
            if mode > 0:
                mode = -mode

        n >>= 1
    return abs(mode)


def gen_num_segments(a):
    n = 0
    for k in a:
        n |= 1 << k
        yield num_segment(n)


def max_seqments(n):
    return reduce(max, gen_num_segments(n))


def main():
    print len(list(pe.dr(10**100, 7)))



    perf()


if __name__ == '__main__':
    main()
