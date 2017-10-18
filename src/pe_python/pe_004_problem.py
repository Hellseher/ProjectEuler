#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  problem-04.py
# Created       :  Mon 30 Mar 2015 21:30:34
# Last Modified :  Wed 19 Aug 2015 07:41:29
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LARGEST PALINDROME PRODUCT
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description]:=-
# A palindromic number reads the same both way. the largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.  Find the largest
# palindrome made from the product of two 3-digit numbers.

import sys
from termcolor import colored


def ispalindrome(n):

    if n == int(str(n)[::-1]):
        return True
    return False


def product():
    """ Returs pruduct of n*n """

    largestPalindrome = 0
    global digit_length
    a = digit_length - 1
    while a >= digit_length:
        if a % 11 == 0:
            b = digit_length - 1
            db = 1
        else:
            b = digit_length - 10
            db = 11

        while b >= a:
            if a*b <= largestPalindrome:
                break
            if ispalindrome(a*b):
                largestPalindrome = a*b
            b = b - db
        a = a - 1
    return largestPalindrome, a, b


def promt(massage):
    if massage == "welcome":
        print colored("Please, enter lenth of the digit", 'blue')
    elif massage == "error":
        print colored("..::Invalid number of arguments::..", 'red')


def main():
    if len(sys.argv) != 2:
        promt("error")
        quit()
    global digit_length
    digit_length = 10 ** int(sys.argv[1])
    print product()


if __name__ == "__main__":
    main()

# TODO nboundLocalError: local variable 'b' referenced before assignment
