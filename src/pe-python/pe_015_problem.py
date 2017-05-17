#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  15-problem.py
# Created       :  Sat 16 May 2015 22:12:37
# Last Modified :  Sat 16 May 2015 23:06:07
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LATTICE PATHS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

#     +->-->+       +->---+     +->---+
#     |  |  v       |  v  |     |  v  |
#     +--+--v       +--+->+     +--+--+
#     !  !  v       !  !  v     !  v  |
#     +--+--+       +-----+     +--+->+
#
#    +-----+       +-----+     +--+--+
#    v  |  |       v  |  |     v  |  |
#    +->+->+       +->+--+     +--+--+
#    !  !  v       !  v  |     v  !  |
#    +--+--+       +--+->+     +->+->+
#
#  How many such routes are there through a 20×20 grid?
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys

import pe


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
    if len(sys.argv) != 3:
        error()  # check error() to edit the massage
    # let's begin
    width = int(sys.argv[1])
    higth = int(sys.argv[2])

    print list(pe.pclrow(width + higth))[width]

    perf()


if __name__ == '__main__':
    main()

# -=:[ References ]:=-
# number of combinations
# binominal cofficient
# Passcal's triangle
