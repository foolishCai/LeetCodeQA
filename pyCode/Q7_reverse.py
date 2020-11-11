#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 14:00
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q7_reverse.py
# @Note    : https://leetcode-cn.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == "-":
            s = s[1:]
            s = -int(s[::-1])
        else:
            s = int(s[::-1])
        if s < -pow(2, 31) or s > pow(2, 31)-1:
            return 0
        else:
            return s
