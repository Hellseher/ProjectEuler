#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  099-problem.py
# Created       :  Wed 16 Sep 2015 22:11:22
# Last Modified :  Wed 16 Sep 2015 23:07:47
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LARGEST EXPONENTIAL
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=99
#
# -=:[ Description ]:=-
# Comparing two numbers written in index form like 211 and 37 is not difficult,
# as any calculator would confirm that 211 = 2048 < 37 = 2187.
#
# However, confirming that 632382518061 > 519432525806 would be much more
# difficult, as both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text
# file containing one thousand lines with a base/exponent pair on each line,
# determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example
# given above.
# <END  OF  DESCRIPTION>-------------------------------------------------------


import time
import math


INIT_TIME = time.time()


# read sourse file, as list of data
with open("../../txt/p099_base_exp.txt", 'r') as f:
    PAIRS = f.read().splitlines()

# define a future max value


def perf():
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    return "Performance time: %s" % millis


def main():
    MAX = 0
    max_pair = []
    for digit in PAIRS:
        base = int(digit.split(",")[0])
        exp = int(digit.split(",")[1])
        checker = math.log10(base) * exp
        if checker > MAX:
            MAX = checker
            max_pair.append(base)
            max_pair.append(exp)
    print perf()
    print max_pair


if __name__ == "__main__":
    main()

# similar
# p122
