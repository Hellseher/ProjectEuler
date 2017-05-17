#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  50-problem.py
# Created       :  Sat 11 Apr 2015 20:57:18
# Last Modified :  Sat 18 Apr 2015 22:21:45
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  CONSECUTIVE PRIME SUM
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/
#
# -=:[ Description ]:=-
# The prime 41, can be written as the sum of six consecutive primes:
#  41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred. The longest sum of consecutive primes below one-thousand that
# adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?


from termcolor import colored
import sys
import time
import math


INIT_TIME = time.time()


def isprime(num):

    search_lim = int(math.sqrt(num))
    for i in xrange(2, search_lim + 1):
        if num % i == 0:
            return False
    return True


def cons_prime_sum(prime_list):
    """ takes a list of prime, return a list with consecutive prime sum """

    pl = []  # prime list of consecutive prime sum
    for p_check in prime_list:
        for p_step in xrange(0, prime_list.index(p_check)):
            for p_index in xrange(p_step, prime_list.index(p_check)):
                pl[::] = []  # clean up list
                get_that_prime = p_index
                while sum(pl) <= p_check:
                    pl.append(prime_list[get_that_prime])
                    get_that_prime += 1
                print pl, p_check


def perf():
    """ Return perfomance time of the programm """

    return ("Perfomance time: %s" % (time.time() - INIT_TIME))


def error():
    """ Massage if error """

    print colored("..::Incorect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():

    if len(sys.argv) != 2:
        error()
    PRIME_LIMIT = int(sys.argv[1])

    PRIME_LIST = []
    for i in xrange(2, PRIME_LIMIT + 1):
        if isprime(i):
            PRIME_LIST.append(i)

    # p_sum = 0
    # for p in PRIME_LIST:
    #     p_sum += p
    #     print p_sum, p
    #     if p_sum > 953:
    #         break

    # print PRIME_LIST
    cons_prime_sum(PRIME_LIST)

    print perf()


if __name__ == '__main__':
    main()
