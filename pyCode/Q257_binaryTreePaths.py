#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 11:11
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q257_binaryTreePaths.py
# @Note    : https://leetcode-cn.com/problems/binary-tree-paths/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths