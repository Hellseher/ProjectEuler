#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  111-problem.py
# Created       :  Thu 22 Oct 2015 19:06:07
# Last Modified :  Thu 22 Oct 2015 22:12:01
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  PRIMES WITH RUNS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net/problem=111
#
# -=:[ Description ]:=-
# Considering 4-digit primes containing repeated digits it is clear that they
# cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and
# so on. But there are nine 4-digit primes containing three ones:
#
# 1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
#
# We shall say that M(n, d) represents the maximum number of repeated digits
# for # an n-digit prime where d is the repeated digit, N(n, d) represents the
# number # of such primes, and S(n, d) represents the sum of these primes.
#
# So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime
# where one is the repeated digit, there are N(4, 1) = 9 such primes, and
# the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0,
# it is only possible to have M(4, 0) = 2 repeated digits, but there are
# N(4, 0) = 13 such cases.
#
# In the same way we obtain the following results for 4-digit primes.  Digit, d
#             M(4, d)     N(4, d)     S(4, d)
#             0           2           13  67061
#             1           3           9   22275
#             2           3           1   2221
#             3           3           12  46214
#             4           3           2   8888
#             5           3           1   5557
#             6           3           1   6661
#             7           3           9   57863
#             8           3           1   8887
#             9           3           7   48073
#
# For d = 0 to 9, the sum of all S(4, d) is 273700.
#
# Find the sum of all S(10, d).
# <END  OF  DESCRIPTION>-------------------------------------------------------


# import ProjectEuler as pe

primes = []
tested = set()

repitit = 10
intint = range(10)
works = []

while len(intint) > 0:
    repitit -= 1
    for w in works:
        try:
            intint.remove(w)
        except:
            pass
    for t in intint:
        print t
        for d in combinations_with_replacement(range(10), 10-repitit):
            for n in permutations([t]*repitit + list(d), 10):
                if n in tested: 
                    continue
                number = int(''.join(map(str, n)))
                tested.add(n)
                if len(str(number)) < 10:
                    continue
                if isprime(number) == True:
                    primes.append(number)
                    works.append(t)

print primes
print len(primes)
print sum(primes)
