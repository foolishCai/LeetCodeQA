#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 17:20
# @Author  : chenyuwei_0303@yeah.net
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q22_generate_parentheses.py
# @url     : https://leetcode-cn.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')