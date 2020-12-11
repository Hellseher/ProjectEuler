#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  55-problem.py
# Created       :  Tue 07 Apr 2015 22:43:45
# Last Modified :  Sun 19 Apr 2015 14:46:00
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LYCHREL NUMBERS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292, 1292 + 2921 = 4213 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196,
# never produce a palindrome. A number that never forms a palindrome through the
# reverse and add process is called a Lychrel number. Due to the theoretical
# nature of these numbers, and for the purpose of this problem, we shall assume
# that a number is Lychrel until proven otherwise. In addition you are given
# that for every number below ten-thousand, it will either (i) become a
# palindrome in less than fifty iterations, or, (ii) no one, with all the
# computing power that exists, has managed so far to map it to a palindrome. In
# fact, 10677 is the first number to be shown to require over fifty iterations
# before producing a palindrome: 4668731596684224866951378664 (53 iterations,
# 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel
# numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
# theoretical nature of Lychrel numbers.


from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    print ("Performance time: %s" % (time.time() - INIT_TIME))


def rev_sum(num, calls=0):
    """ Takes num, returns summarised value with reversed """

    if calls == 100:
        return num, calls
    if str(num) == str(num)[::-1]:
        return num, calls
    return rev_sum((int(num) + int(str(num)[::-1])), calls + 1)


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
    LYCHREL_NUM = []

    for i in xrange(10, num):
        LYCHREL_POLY = 0  # find polindrome Lychrel numbers
        if i == int(str(i)[::-1]):
            LYCHREL_POLY = i * 2
            if rev_sum(LYCHREL_POLY)[1] == 100:
                LYCHREL_NUM.append(i)
        if rev_sum(i)[1] == 100:
            LYCHREL_NUM.append(i)

    print_out(LYCHREL_NUM)
    # print ("\nQuantity of Lychrel numbers: %s" % len(LYCHREL_NUM))

    # perf()


if __name__ == '__main__':
    main()
