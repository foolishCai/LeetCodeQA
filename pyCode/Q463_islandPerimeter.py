# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/30 17:11
# @Author : Cai
# @Email : chenyuwei_0303@yeah.net
# @File : Q463_islandPerimeter.py
# @Note : https://leetcode-cn.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        residue = [0]*len(grid[0])
        ans = 0
        for i in grid:
            flag = True
            if sum(i) == 0:
                continue
            for j, c in enumerate(i):
                if c == 1:
                    if flag:
                        ans += 4 - residue[j]*2 #跟上一行比
                        flag = False #跟前一个比
                    else:
                        ans += 2 - residue[j]*2
                else:
                    flag = True
            residue = i
        return ans
