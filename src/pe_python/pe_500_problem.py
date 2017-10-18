#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  500-problem.py
# Created       :  Sun 12 Apr 2015 00:55:17
# Last Modified :  Sun 12 Apr 2015 22:37:22
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# License       :  Same as Python (GPL)
# Credits:
#
"""
..:: Description ::..


"""

# from math import sqrt
import time
import sys


INIT_TIME = time.time()


def bigdev(limit):
    number = 0
    dev = 0
    while dev != limit:

        dev = 0
        number += 1
        for i in xrange(1, number + 1):
            if number % i == 0:
                dev += 1

    return number


def main():
    if len(sys.argv) != 2:
        quit()
    # num = int(sys.argv[1])

    fucking_big_dev = 2**500500
    print bigdev(fucking_big_dev) // 500500507
    print "Perfomance time %s" % (time.time() - INIT_TIME)


if __name__ == '__main__':
    main()
