#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 8:54
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q222_countNodes.py
# @Note    : https://leetcode-cn.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)

