#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 9:00
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q190_reverseBits.py
# @Note    : https://leetcode-cn.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret