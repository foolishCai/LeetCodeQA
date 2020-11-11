#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 18:11
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q200_ilands_numbers.py
# @Note    : https://leetcode-cn.com/problems/number-of-islands/solution/pythonjavascript-tao-lu-dfs200-dao-yu-shu-liang-by/


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)