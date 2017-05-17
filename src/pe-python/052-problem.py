#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  52-problem.py
# Created       :  Thu 21 May 2015 00:08:44
# Last Modified :  Fri 22 May 2015 23:07:32
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PERMUTED MULTIPLES
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
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


def divchk(num, multls):
    """ Check if digits of num the same as multiplied by multls. """
    for m in multls:
        if "".join(sorted(str(num))) != "".join(sorted(str(num*m))):
            return False
    return True

def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    step = 1
    multis = [2, 3, 4, 5, 6, 7]

    while True:
        if divchk(step, multis):
            print step
            break
        step += 1

    perf()



if __name__ == '__main__':
    main()
