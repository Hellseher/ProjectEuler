#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  48-problem.py
# Created       :  Thu 09 Apr 2015 01:08:53
# Last Modified :  Sat 18 Apr 2015 22:21:07
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  SELF POWER
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# the series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series to 1**1 + 2**2 + .. + 1000**1000


from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    print ("Performance time: %s" % (time.time() - INIT_TIME))


def self_pow(num):
    """ Takes num, returns powered summarised value """

    powerd_sum = 0
    for i in xrange(1, num + 1):
        powerd_sum += i**i
    return powerd_sum


def error():
    """ Arguments checking """

    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def print_out(give_list):
    for i in give_list:
        if give_list.index(i) % 10 == 0:
            print "\r"
        print i,


def main():

    if len(sys.argv) != 2:
        error()
    num = int(sys.argv[1])

    print self_pow(num) - (self_pow(num) // 10**10) * 10**10
    perf()


if __name__ == '__main__':
    main()
