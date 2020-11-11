#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 18:12
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q445_add_two_numbers.py
# @Note    :
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        head = ListNode(0)
        carry = 0
        while stack1 or stack2 or carry:
            s1 = stack1.pop() if stack1 else 0
            s2 = stack2.pop() if stack2 else 0
            cur = s1 + s2 + carry
            carry = 1 if cur >= 10 else 0
            cur = cur % 10
            curNode = ListNode(cur)
            curNode.next = head.next
            head.next = curNode
        return head.next

l1 = [7,2,4,3]
l2 = [5,6,4]