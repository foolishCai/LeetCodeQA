#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 8:48
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q435_eraseOverlapIntervals.py
# @Note    : https://leetcode-cn.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda a: a[1])
        n = len(intervals)
        end, count = -float('inf'), 0
        for inter in intervals:
            start = inter[0]
            if start >= end:
                count += 1
                end = inter[1]
        return n - count
