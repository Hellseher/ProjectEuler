#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  254-problem.py
# Created       :  Fri 01 May 2015 19:18:21
# Last Modified :  Sat 06 Jun 2015 08:52:29
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  SUMS OF DIGIT FACTORIALS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
#
# -=:[ Description ]:=-
#    Define f(n) as the sum of the factorials of the digits of n. For example,
#    f(342) = 3! + 4! + 2! = 32.
#
#    Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 =
#    5.bit_length Define g(i) to be the smallest positive integer n such that
#    sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be verified
#    that g(5) is 25.
#
#    Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 =
#    7.bit_length Further, it can be verified that g(20) is 267 and ∑ sg(i) for
#    1 ≤ i ≤ 20 is 156.
#
#    What is ∑ sg(i) for 1 ≤ i ≤ 150? """
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys

import ProjectEuler as pe


INIT_TIME = time.time()


def perf():
    # show the performance time
    millis = time.time() - INIT_TIME
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
    take_num = int(sys.argv[1])  # taken arg from the user
    g_num = []

    # show all possible combination for factorial sums
    for i in xrange(1, take_num + 1):
        g = 1
        got_it = 0
        while True:
            got_it = pe.ds(pe.dfs(g))
            if got_it == i:
                print "%s \t: %s" % (pe.dsfs(g), g)
                g_num.append(g)
                break
            g += 1

    g_num_sum = 0
    for g in g_num:
        g_num_sum += pe.ds(g)

    print "Final digit sum: %s" % g_num_sum

    perf()


if __name__ == '__main__':
    main()
