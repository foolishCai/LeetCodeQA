#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 15:13
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q216_combinationSum3.py
# @Note    : https://leetcode-cn.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        ns = [i + 1 for i in range(9)]

        def find(s, sum_now, use):
            if len(use) == k:
                if sum_now == n:
                    ans.append(use)
                    return
                else:
                    return

            for i in range(s, len(ns) - (k - len(use)) + 1):
                find(i + 1, sum_now + ns[i], use + [ns[i]])

        find(0, 0, [])

        return ans
