#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 8:50
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q342_isPowerOfFour.py
# @Note    : https://leetcode-cn.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while 4 ** i <= n:
            if 4 ** i == n:
                return True
            else:
                i += 1
        return False