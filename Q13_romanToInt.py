#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 16:14
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q13_romanToInt.py
# @Note    : https://leetcode-cn.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1,
             'IV': 3,
             'V': 5,
             'IX': 8,
             'X': 10,
             'XL': 30,
             'L': 50,
             'XC': 80,
             'C': 100,
             'CD': 300,
             'D': 500,
             'CM': 800,
             'M': 1000
        }
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
