#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  92-problem.py
# Created       :  Mon 27 Apr 2015 20:29:50
# Last Modified :  Mon 27 Apr 2015 21:13:40
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


INIT_TIME = time.time()


def perf():
    # show the performance time
    millis = int(time.time() - INIT_TIME)
    print("Performance time: %s" % millis)


def error():
    # massage if not supported entering

    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()



def square_digits(num):
    """ Return the sum of squares of the base-10 digits of num. """
    total = 0
    for d in str(num):
        total += int(d) ** 2
    return total


def square_digit_chain(num):
    """ takes integer number,
        returns square digit chain of it and 1 or 89 end up."""

    num_to_str = str(num)
    digit_chain = []
    while True:
        digit_square_sum = 0
        for n in num_to_str:
            digit_square_sum += int(n)**2
        digit_chain.append(digit_square_sum)
        num_to_str = str(digit_square_sum)

        if digit_square_sum == 89 or digit_square_sum == 1:
            return digit_square_sum, digit_chain


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    taken_num = int(sys.argv[1])
    count_89 = 0

    for i in xrange(1, taken_num):
        if square_digit_chain(i)[0] == 89:
            count_89 += 1
    print count_89

    perf()


if __name__ == '__main__':
    main()
