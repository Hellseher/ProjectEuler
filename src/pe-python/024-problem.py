#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  24-problem.py
# Created       :  Thu 11 Jun 2015 07:21:01
# Last Modified :  Fri 19 Jun 2015 07:21:19
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  LEXICOGRAPHIC PERMUTATIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=24
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
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    return "Performance time: %s" % millis


def error():
    ''' Massage if not supported entering '''
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def next_permutation(get_list):
    ''' Computes the next lexicographical permutation of the specified list in
    place, returning whether a next permutation existed. '''
    i = len(get_list) - 1
    while i > 0 and get_list[i - 1] >= get_list[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(get_list) - 1

    while get_list[j] <= get_list[i - 1]:
        j -= 1
    get_list[i - 1], get_list[j] = get_list[j], get_list[i - 1]

    get_list[i : ] = get_list[len(get_list) - 1 : i - 1 : -1]
    
    return True

def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    lex_len = int(sys.argv[1])

    get_list = range(lex_len)
    step = 1
    while True:
        print step
        step += 1
        next_permutation(get_list)
        if step == 1000000:
            print get_list
            print perf()
            break



if __name__ == '__main__':
    main()


# -=:[ Reference ]:=-
# [1]

# -=:[ Links ]:=-
# [1] nayuki.io
