#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  16-problem.py
# Created       :  Sat 16 May 2015 21:36:58
# Last Modified :  Sat 16 May 2015 21:39:31
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
#
#
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
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    power_limit = int(sys.argv[1])

    print pe.ds(2**power_limit)
    perf()


if __name__ == '__main__':
    main()
