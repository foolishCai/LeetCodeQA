#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 09:02
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q14_longestCommonPrefix.py
# @Note    : https://leetcode-cn.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans
