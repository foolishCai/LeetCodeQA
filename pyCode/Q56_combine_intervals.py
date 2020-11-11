#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 18:18
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q56_combine_intervals.py
# @Note    : https://leetcode-cn.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x[0])
        result = list()
        for item in intervals:
            if not result or result[-1][1] < item[0]:
                result.append(item)
            else:
                result[-1][1] = max(result[-1][1], item[1])

        return result