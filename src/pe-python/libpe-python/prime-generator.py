#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  primes.py
# Created       :  Wed 01 Apr 2015 23:05:02
# Last Modified :  Thu 14 May 2015 00:13:00
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PRIME NUMBER GENERATOR
# License       :  Same as Python (GPL)
# Credits:
#
"""
..:: Description ::..

Prime number generator.
"""


from termcolor import colored
import os
import sys
import time

import pe


# Current location
PWD = os.getcwd()
FILENAME = "primes"
# Full path to the file
FULL_PATH = os.path.join(PWD, FILENAME)
INIT_TIME = time.time()


def readf(f):
    """ Read file as a list and close it """

    with open(f, 'r') as open_file:
        of = open_file.read().splitlines()
    return of


def writef(f, data):
    """ Write to the end of  file and close it """

    with open(f, 'a') as writen_file:
        writen_file.write(str(data) + '\n')


def perf():
    """ Show the performance time """
    millis = int(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def main():
    # TODO  don't have to read all the file
    #       just read the last line of it

    if os.path.exists(FULL_PATH):
        PRIME_LIST = readf(FULL_PATH)
    else:
        print("wrong")
        quit()
    print("Old last record: %s" % PRIME_LIST[-1])  # last records of the list

    LAST_PRIME = int(PRIME_LIST[-1]) + 1
    NEW_PRIME_LIMIT = LAST_PRIME * 2
    for p in xrange(LAST_PRIME, NEW_PRIME_LIMIT + 1):
        if pe.isp(p):
            writef(FULL_PATH, p)

    print("New last record: %s" %  readf(FULL_PATH)[-1])
    perf() # Show up time of script.


if __name__ == "__main__":
    main()
