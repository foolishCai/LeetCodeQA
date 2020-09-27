#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 13:42
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q226_invertTree.py
# @Note    : https://leetcode-cn.com/problems/invert-binary-tree/solution/226fan-zhuan-er-cha-shu-by-yi-wen-statistics/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
