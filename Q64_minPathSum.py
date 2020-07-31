#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 10:22
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q64_minPathSum.py
# @Note    :

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
