#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  357-problem.py
# Created       :  Fri 03 Jul 2015 08:52:15
# Last Modified :  Sat 14 Nov 2015 21:41:23
# Maintainer    :  sharlaran, <sharlatanus@gmail.com>
# title         :  PRIME GENERATING INTEGERS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=357
#
# -=:[ Description ]:=-
# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
# 
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.
# <END  OF  DESCRIPTION>-------------------------------------------------------


from termcolor import colored
import time
import sys

import ProjectEuler as pe


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

def prime_gen_int(num, take_list):
    '''Return True if all d+n/d == prime'''
    for divisor in take_list:
        print (divisor + num) / divisor
        #if not pe.isp((divisor + num)/ divisor):
            #return False
    #return True


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin

    gen_lim = int(sys.argv[1])

    for num in xrange(3, gen_lim+1):
        #if not pe.isp(num):
        give_list =  list(pe.factors(num))
        print give_list
            #if prime_gen_int(num, give_list):
            #print give_list
        prime_gen_int(num, give_list),

    print perf()


if __name__ == '__main__':
    main()
