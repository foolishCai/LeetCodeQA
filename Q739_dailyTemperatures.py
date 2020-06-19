#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 13:28
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q739_dailyTemperatures.py
# @Note    :


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10**9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
