#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  01-problem.py
# Created       :  Tue 24 Mar 2015 23:19:00
# Last Modified :  Sun 16 Oct 2016 22:22:31 sharlatan
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  MULTIPLES OF 3 AND 5
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ Description ]:=-
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get  3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

sum_mult = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_mult += i
print(sum_mult)
