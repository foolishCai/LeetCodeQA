#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 8:45
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q454_fourSumCount.py
# @Note    : https://leetcode-cn.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, A, B, C, D):
        res = 0
        dic = {}
        for a in A:
            for b in B:
                total1 = a + b
                dic[total1] = dic.get(total1, 0) + 1
        for c in C:
            for d in D:
                total2 = c + d
                if -total2 in dic:
                    res += dic[-total2]
        return res
