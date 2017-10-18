#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  gridprint.py
# Created       :  Sat 04 Apr 2015 00:26:37
# Last Modified :  Sat 04 Apr 2015 23:03:49
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# License       :  Same as Python (GPL)
# Credits:
#
"""
..:: Description ::..

print to stdo by terminal width
"""


from subprocess import call


TERM_WIDTH = call(["tput", "cals"])


L = [x*2 for x in range(0, 40)]
total_len
print L
