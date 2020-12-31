#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 9:18
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q101_isSymmetric.py
# @Note    :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #方法一：应用层序遍历的思想
        if not root:
            return True
        #应用队列，按层压入树节点
        queue=collections.deque()
        queue.append(root)
        while queue:
            level_val=[]#用来保存树每一层节点的值
            for _ in range(len(queue)):
                temp=queue.popleft()
                if not temp:
                    level_val.append(-1)#为了区分特殊情况
                    continue
                level_val.append(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
            if level_val[:]==level_val[::-1]:#对称数组的判定
                continue
            else:
                return False
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isSym(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
            return False

        return isSym(root.left, root.right)
