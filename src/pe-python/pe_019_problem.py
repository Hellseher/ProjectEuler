#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  19-problem.py
# Created       :  Sat 02 May 2015 23:44:28
# Last Modified :  Fri 04 Sep 2015 22:48:20
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  COUNTING SUNDAYS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# You are given the following information, but you may prefer to do some
# research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years,  twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not
# on a century unless it is divisible by 400.  How many Sundays fell on the
# first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# <END  OF  DESCRIPTION>-------------------------------------------------------


import time
import sys

from termcolor import colored


INIT_TIME = time.time()
MONTHS = {
    'Jan': 366,
    'Feb': 32,
    'Mar': 60,
    'Apr': 91,
    'May': 121,
    'Jun': 152,
    'Jul': 182,
    'Aug': 213,
    'Sep': 244,
    'Oct': 274,
    'Nov': 305,
    'Dec': 335,
}

LEAP_MONTHS = {
    'Jan': 367,
    'Feb': 32,
    'Mar': 61,
    'Apr': 92,
    'May': 122,
    'Jun': 153,
    'Jul': 183,
    'Aug': 214,
    'Sep': 245,
    'Oct': 275,
    'Nov': 306,
    'Dec': 336,
}


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
    if len(sys.argv) != 3:
        error()  # check error() to edit the massage
    # let's begin
    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])

    days_ribon = 1
    first_sunday = 0

    for year in range(start_year, end_year + 1):

        # normal year
        if year % 4 != 0 or year % 100 == 0:
            days = 365
            for day in range(days_ribon, days_ribon + days):
                for first_of_month in MONTHS.values():
                    if day % 7 == 0 and day % first_of_month == 0:
                        first_sunday += 1

        # leap year
        elif year % 4 == 0 and year % 100 != 0:
            days = 366
            for day in range(days_ribon, days_ribon + days):
                for first_of_month in LEAP_MONTHS.values():
                    if day % 7 == 0 and day % first_of_month == 0:
                        first_sunday += 1

        days_ribon += days

    print first_sunday
    perf()


if __name__ == '__main__':
    main()
