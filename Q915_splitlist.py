#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 18:14
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q915_splitlist.py
# @Note    : https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals/


class Solution:
    def partitionDisjoint(self, A):
        maxIndex = 0
        leftMax = A[0]
        tmp = A[0]
        for i in range(1, len(A)):
            tmp = max(tmp, A[i])
            if A[i] < leftMax:
                maxIndex = i
                leftMax = tmp
        return maxIndex+1