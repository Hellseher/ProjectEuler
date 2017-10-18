#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  030-problem.py
# Created       :  Fri 21 Aug 2015 07:18:30
# Last Modified :  Fri 21 Aug 2015 07:38:32
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
#
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    return "Performance time: %s" % millis


def error():
    ''' Massage if not supported entering '''
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin

    # brute force
    step = 1
    final_sum = 0
    while True:
        power_some = 0
        for digit in str(step):
            power_some = int(digit) ** 5

        if step == power_some:
            print "Find it! %d " % step
            final_sum += step
            print "And the Final Summ is %d " % final_sum

        step += 1

    perf()


if __name__ == '__main__':
    main()
