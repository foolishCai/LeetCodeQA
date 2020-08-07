#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 14:27
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q100_isSameTree.py
# @Note    : https://leetcode-cn.com/problems/same-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if (p != None and q == None) or (p == None and q != None)  :
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
