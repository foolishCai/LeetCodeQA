# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/29 10:49
# @Author : Cai
# @Email : chenyuwei_0303@yeah.net
# @File : Q129_sumNumbers.py
# @Note : https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, presum):
            if not node:
                return None
            if not node.left and not node.right:
                self.res += presum * 10 + node.val
                return
            presum = 10 * presum + node.val
            dfs(node.left, presum)
            dfs(node.right, presum)
        dfs(root, 0)
        return self.res