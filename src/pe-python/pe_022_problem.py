#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  22-problem.py
# Created       :  Fri 05 Jun 2015 07:35:55
# Last Modified :  Wed 16 Sep 2015 22:17:15
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  NAME SCORES
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
# <END  OF  DESCRIPTION>-------------------------------------------------------


import string


INIT_TIME = time.time()


with open("../../txt/p022_names.txt", 'r') as f:
    NAMES = sorted(f.read().replace('\"','').split(','))


def perf():
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    print "Performance time: %s" % millis


def letter_to_num(getstring):
    ''' Return the sum of letter num values. '''
    alpha_upper =  string.ascii_uppercase
    sum_alpha = 0
    for s in getstring:
        sum_alpha += alpha_upper.index(s)+1
    return sum_alpha


def main():
    # let's begin
    global NAMES
    total_sum = 0

    for n in NAMES:
        total_sum += (NAMES.index(n)+1) * letter_to_num(n)

    print total_sum

    perf()


if __name__ == '__main__':
    main()
