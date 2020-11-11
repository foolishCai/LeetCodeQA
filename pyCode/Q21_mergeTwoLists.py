#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 08:11
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q21_mergeTwoLists.py
# @Note    : https://leetcode-cn.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

