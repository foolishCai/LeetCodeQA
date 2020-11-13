#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 8:53
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q70_climbStairs.py
# @Note    : https://leetcode-cn.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [None]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

