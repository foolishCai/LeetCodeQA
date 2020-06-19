#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 09:34
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q5_longestPalindrome.py
# @Note    : https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #dp[i][j] = true,if s[i] = s[j] ....
        #dp[0][len(s)-1]
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        res = 0, 0 #长度为1时
        for i in range(1, length):
             for j in range(length-i):
                if s[j] == s[j+i] and (j+1 >= j+i-1 or dp[j+1][j+i-1]):
                    dp[j][j+i] = 1
                    res = j, j+i
        left, right = res
        return s[left: right+1]
