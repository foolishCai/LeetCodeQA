#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 21:50
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q96_numTrees.py
# @Note    : https://leetcode-cn.com/problems/unique-binary-search-trees/

from functools import lru_cache

class Solution:
    @lru_cache()
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 1
        if n <= 2:
            return n
        return sum([self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n + 1)])
