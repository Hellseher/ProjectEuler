#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  17-problem.py
# Created       :  Sun 26 Apr 2015 22:57:00
# Last Modified :  Thu 14 May 2015 00:13:08
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  NUMBER LETTER COUNTS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# #forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys
import numspell
gm = numspell.Speller('en')


INIT_TIME = time.time()


def perf():
    # show the perfomance time
    millis = int(time.time() - INIT_TIME)
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
    get_limit = int(sys.argv[1])
    total = 0
    for n in xrange(1, get_limit):
        for s in gm.spell(n):
            if s != "-" and s != " ":
                total += 1

    total += 99*3 * 9
    print total
    perf()


if __name__ == '__main__':
    main()


# -=:[ Links ]:=-
# [1] https://github.com/alco/numspell
