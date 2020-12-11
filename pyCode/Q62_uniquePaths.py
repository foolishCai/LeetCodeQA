#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 8:34
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q62_uniquePaths.py
# @Note    : https://leetcode-cn.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m]*n
        for i in range(m):
            dp[0][i]=1
        for i in range(n):
            dp[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]