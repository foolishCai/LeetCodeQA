#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 9:07
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q203_removeElements.py
# @Note    :

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head