#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 09:39
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q67_addBinary.py
# @Note    : https://leetcode-cn.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        else:
            x = 0
            for i in range(1, len(a) + 1):
                x += int(a[-i]) * pow(2, i - 1)
            for i in range(1, len(b) + 1):
                x += int(b[-i]) * pow(2, i - 1)
            y = ''
            while x > 0:
                x, z = divmod(x, 2)
                y = str(z) + y
            return y