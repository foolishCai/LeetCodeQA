#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 10:15
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q120_minimumTotal.py
# @Note    :

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])
