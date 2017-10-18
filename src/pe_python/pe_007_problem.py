#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  07-problem.py
# Created       :  Mon 30 Mar 2015 20:40:11
# Last Modified :  Sun 19 Apr 2015 15:10:23
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  10001ST PRIME
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,
# we can see that the
# 6th prime is 13what is the 10001st prime number?


from math import sqrt


def isprime(n):

    for i in xrange(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    prime_10001 = []
    candidate = 1

    while len(prime_10001) != 10001:
        if isprime(candidate):
            prime_10001.append(candidate)
        candidate += 2

    print prime_10001[10000]


if __name__ == "__main__":
    main()
