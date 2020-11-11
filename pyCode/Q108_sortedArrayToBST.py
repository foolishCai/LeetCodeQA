#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 19:31
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q108_sortedArrayToBST.py
# @Note    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
