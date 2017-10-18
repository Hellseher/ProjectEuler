#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  02-problem.py
# Created       :  Sat 04 Apr 2015 23:04:28
# Last Modified :  Sun 19 Apr 2015 14:23:42
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  EVEN FIBONACCI NUMBERS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... , F(n-1) + F(n+1)
# By considering the terms in the Fibonacci sequence whose values do not exceed
# fou million, find the sum of the even-valued terms.


from termcolor import colored
import sys
import time


INIT_TIME = time.time()


def fi_num(n):
    """ Return n's Fibonacci number """

    if n < 2:
        return n
    before = 1
    now = 1
    for num in xrange(2, n):
        before, now = now, now + before
    return now


def error():
    """ Massage if error entering """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():

    if len(sys.argv) != 2:
        error()

    limit = int(sys.argv[1])
    step = 0
    fi_sum = 0
    fi_check = 0
    print ("The %s's Fibonacci is: %s" % (limit, fi_num(limit)))

    while fi_check < limit:
        fi_check = fi_num(step)
        if fi_check % 2 == 0:
            fi_sum += fi_check
        step += 1
    print "Sum of even Fibonacci numbers less then %s: %s" % (limit, fi_sum)


if __name__ == "__main__":
    main()
    print ("Perfomence time: %s" % (time.time() - INIT_TIME))
