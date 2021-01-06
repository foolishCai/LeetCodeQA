#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 8:44
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q509_fib.py
# @Note    : https://leetcode-cn.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = self.fib(n-1)
            b = self.fib(n-2)
            return a+b