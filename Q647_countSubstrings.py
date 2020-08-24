#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 21:23
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q647_countSubstrings.py
# @Note    : https://leetcode-cn.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):  # 奇数子串的情况
            res += self.expand(s, i, i)

        for j in range(len(s)):  # 偶数子串的情况
            res += self.expand(s, j, j + 1)

        return res

    def expand(self, s, l, r):
        count = 0
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:  # 下标不越界且为回文子串则继续循环
            l -= 1
            r += 1
            count += 1
        return count

