#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  pe.py
# Created       :  Mon 27 Apr 2015 19:01:22
# Last Modified :  Wed 29 Apr 2015 23:03:31
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# Title         :
# License       :  Same as Python (GPL)
# Credits       :
#
# -=:[ Description ]:=-
#
#
# <END  OF  DESCRIPTION>-------------------------------------------------------


import math


def isp(num):
    """
    Check num for primirity.
    """
    if num == 1:
        return False
    elif num < 4:
        return True  # 2 and 3 are primes
    elif num % 2 == 0:
        return False
    elif num < 9:  # already excluded 4, 6 and 8.
        return True
    elif num % 3 == 0:
        return False
    else:
        r = int(math.sqrt(num))  # rounded r so that r*r <= num
        f = 5
        while f <= r:
            if num % f == 0:
                return False
            elif num % (f + 2) == 0:
                return False
            f += 6
    return True


def numspell(num):
    NUMBERS = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    ORDERS  = ["", "thousand", "million", "billion", "trillion", "quadrillion",
                "quintillion", "sextillion", "septillion", "octillion",
                "nonillion", "decillion", "undecillion", "duodecillion",
                "tredecillion", "quattuordecillion", "sexdecillion",
                "septendecillion", "octodecillion", "novemdecillion",
               "vigintillion "]

    SPELL_IT = []  # future list of spelled numbers
    num_to_str = str(num)
    num_str_len = len(num_to_str)
    groups = (num_str_len + 2) / 3
    num_to_str = num_to_str.zfill(groups * 3)
    if num == 0:
        SPELL_IT.append("zero")
    else:
        for i in range(0, groups*3, 3):
            h = int(num_to_str[i])
            t = int(num_to_str[i+1])
            u = int(num_to_str[i+2])
            g = groups - (i / 3 + 1)

            if h >= 1:
                SPELL_IT.append(one_to_nine[h])
                SPELL_IT.append("hundred")
                if t != 0 or u != 0:
                    SPELL_IT.append("and")
            if t > 1:
                SPELL_IT.append(ten_to_ninety[t])
            if u >= 1:
                SPELL_IT.append(one_to_nine[u])
            elif t == 1:
                if u >= 1:
                    SPELL_IT.append(eleven_to_nineteen[u])
                else:
                    SPELL_IT.append(ten_to_ninety[t])
            else:
                if u >= 1:
                    SPELL_IT.append(one_to_nine[u])

            if g >= 1 and (h + t + u) > 0:
                SPELL_IT.append(thousand_to_vigintillion[g])
    return SPELL_IT


def main():
    print numspell(111)


if __name__ == '__main__':
    main()
