#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  268-problem.py
# Created       :  Fri 05 Jun 2015 06:27:06
# Last Modified :  Fri 05 Jun 2015 22:24:35
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  Numberw with prime factors less then 100
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# It can be verified that there are 23 positive integers less than 1000 that
# are divisible by at least four distinct primes less than 100.
# Find how many positive integers less than 10^16 are divisible by at least four
# distinct primes less than 100.
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
    perf()


if __name__ == '__main__':
    main()
