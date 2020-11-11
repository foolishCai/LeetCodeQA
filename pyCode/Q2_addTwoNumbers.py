#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 21:31
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q2_addTwoNumbers.py
# @Note    : https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0);
        curr = head
        carry = 0
        while carry > 0 or l1  or l2:
            sum = carry
            sum += l1.val if l1 else 0
            sum += l2.val if l2 else 0
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        return head.next