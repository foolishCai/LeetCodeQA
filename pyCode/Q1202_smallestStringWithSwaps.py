#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 9:16
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1202_smallestStringWithSwaps.py
# @Note    : https://leetcode-cn.com/problems/smallest-string-with-swaps/

import collections
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = {i: i for i in range(len(s))}  # 初始化并查集

        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)
            # 合并可交换位置
        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)
        # 排序
        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)
            for i, c in zip(sorted(q), t):
                ans[i] = c
        return ''.join(ans)