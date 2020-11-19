#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 8:46
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q83_deleteDuplicates.py
# @Note    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        head.next = self.deleteDuplicates(head.next)

        if head.val == head.next.val:
            return head.next
        else:
            return head

