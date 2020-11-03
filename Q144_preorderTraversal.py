# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 17:33
# @Author : Cai
# @Email : chenyuwei_0303@yeah.net
# @File : Q144_preorderTraversal.py.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, res = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return res