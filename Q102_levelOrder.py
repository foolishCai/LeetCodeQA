#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 14:27
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q102_levelOrder.py
# @Note    : https://leetcode-cn.com/problems/binary-tree-level-order-traversal/



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []  # 存储最终结果的大列表

    # 增加一个参数表示层级，注意使用参数形式传递，这样子不会有全局干扰
    def levelOrder(self, root: TreeNode, level=0):
        # 如果节点为空。直接返回一个空列表。根节点为空返回这个结果。子节点为空，相当于回退，不影响
        if not root:
            return []
        # print((root.val,level)) #调试用

        # 如果当前层的子列表不存在，先新增一个空列表,后续再根据层值去插值
        if len(self.res) <= level:
            self.res.append([])

        print(self.res)
        self.res[level].append(root.val)
        level += 1  # 更新层级
        self.levelOrder(root.left, level)
        self.levelOrder(root.right, level)
        return self.res