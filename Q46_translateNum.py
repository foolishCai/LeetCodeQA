#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 09:29
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q46_translateNum.py
# @Note    : https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/

class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a