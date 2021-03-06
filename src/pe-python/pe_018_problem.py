#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  18-problem.py
# Created       :  Sat 11 Apr 2015 23:59:20
# Last Modified :  Sat 18 Apr 2015 17:46:43
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :  MAXIMUM PATH SUM I
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# ..:: Description ::..
#
# By starting at the top of the triangle below and moving to
# adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
data = """75
          95 64
          17 47 82
          18 35 87 10
          20 04 82 47 65
          19 01 23 75 03 34
          88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
          53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
          91 71 52 38 17 14 91 43 58 50 27 29 48
          63 66 04 68 89 53 67 30 73 16 69 87 40 31
          04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
#
# NOTE: As there are only 16384 routes, it is possible to solve
# this problem by trying every route. However, Problem 67, is the
# same challenge with a triangle containing one-hundred rows; it
# cannot be solved by brute force, and requires a clever method! ;o)


def solve(tri):
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        tri.append([max(t0[i], t0[i+1]) + t for i, t in enumerate(t1)])
    return tri[0][0]


def left_sum(get_list):
    """ takes a list and return the sum of last elements """

    give_left_sum = []
    for i in get_list:
        give_left_sum.append(int(i[:-1]))
    return sum(give_left_sum)


def right_sum(get_list):
    """ takes a list and return the sum of first elements """

    give_right_sum = []
    for i in get_list:
        give_right_sum.append(int(i[0]))
    return sum(give_right_sum)


def main():
    print solve([map(int, row.split()) for row in data.splitlines()])


if __name__ == '__main__':
    main()
