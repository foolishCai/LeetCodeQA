#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 09:45
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q221_maxmalSquare.py
# @Note    : https://leetcode-cn.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]=="1"):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res*res
