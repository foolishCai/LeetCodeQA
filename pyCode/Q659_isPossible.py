#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 8:41
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q659_isPossible.py
# @Note    : https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            for v in res:
                if n == v[-1] + 1:
                    v.append(n)
                    break
            else:
                res.insert(0, [n])

        return all([len(v) >= 3 for v in res])