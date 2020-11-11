#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 20:10
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q112_hasPathSum.py
# @Note    : https://leetcode-cn.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right