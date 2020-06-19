#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 09:26
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q1014_maxScoreSightseeingPair.py
# @Note    : https://leetcode-cn.com/problems/best-sightseeing-pair/


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        pre_max = A[0] + 0  # 初始值
        for i in range(1, len(A)):
            res = max(res, pre_max + A[i] - i)
            pre_max = max(pre_max, A[i] + i)
        print(res)