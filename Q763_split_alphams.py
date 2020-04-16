#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 19:43
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q763_split_alphams.py
# @Note    : https://leetcode-cn.com/problems/partition-labels/solution/enumerateyu-zi-dian-de-shi-yong-by-shao-shuai-5/

class Solution:
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        start = 0
        end = 0
        res = []

        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res