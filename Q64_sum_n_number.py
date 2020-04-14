#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 19:35
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q64_sum_n_number.py
# @Note    :
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


class Solution:
    def sumNums(self, n):
        ans = n
        if n-1 <= 0:
            return ans
        else:
            ans = ans + self.sumNums(n-1)
            return ans

