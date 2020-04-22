#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 16:17
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q199_rightSideView.py
# @Note    : https://leetcode-cn.com/problems/binary-tree-right-side-view/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        ans, nodes = [], [root]
        while nodes:
            ans.append(nodes[-1].val)
            nodes = [n for node in nodes for n in [node.left, node.right] if n]
        return ans
