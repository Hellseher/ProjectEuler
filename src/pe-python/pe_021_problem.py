#! /usr/bin/env python
# _*_ coding : UTF-8 _*_
# File       :  pe_021_problem.py
# Created    : <2017-8-11 Fri 01:03:50 BST>
# Modified   : <2017-8-11 Fri 01:41:24 BST> sharlatan
# Maintainer :  sharlatan, <sharlatanus@gmail.com>
# Title      :  AMICABLE NUMBERS
# License    :  Same as Python (GPL)
# Credits    :  https://projecteuler.net

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import sys
sys.path.append('../../lib/py/')

import ProjectEuler as pe


for i in range(10000):
    print i, 
    for j in list(pe.proper_devisors(i)):
        print j,
    print
