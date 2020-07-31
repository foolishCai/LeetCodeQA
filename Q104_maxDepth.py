#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:45
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q104_maxDepth.py
# @Note    : https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
