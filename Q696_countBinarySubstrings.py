#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 10:03
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q696_countBinarySubstrings.py
# @Note    : https://leetcode-cn.com/problems/count-binary-substrings/


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        cur = 1
        prev = 0
        res = 0
        for i in range(1, length):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, prev)
                prev = cur
                cur = 1
        return res + min(cur, prev)