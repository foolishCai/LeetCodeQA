#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 9:03
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1128_numEquivDominoPairs.py
# @Note    : https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/

import collections

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        ans = 0
        d = collections.defaultdict(int)
        # step1
        for i, j in dominoes:
            num = 10 * i + j if i < j else 10 * j + i
            d[num] += 1
        # step2
        for k in d.values():
            ans += int(k * (k - 1) / 2)
        return ans