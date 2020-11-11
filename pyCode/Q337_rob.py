#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 10:28
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q337_rob.py
# @Note    : https://leetcode-cn.com/problems/house-robber-iii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pres = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.pres:
            return self.pres[root]
        self.pres[root] = max(self.rob(root.left)+self.rob(root.right), root.val+(0 if not root.left else self.rob(root.left.left)+self.rob(root.left.right))+(0 if not root.right else self.rob(root.right.left)+self.rob(root.right.right)))
        return self.pres[root]