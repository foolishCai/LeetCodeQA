#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 8:54
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q147_insertionSortList.py
# @Note    : https://leetcode-cn.com/problems/insertion-sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur, nxt = head, head.next
        dummy = ListNode(float('-inf'))
        dummy.next = head  # 返回用
        while nxt:
            if nxt.val >= cur.val:  # 若第二个值比第一个值大  不处理  指针都后移
                cur = nxt
                nxt = nxt.next
            else:  # 否则就插入
                cur.next = nxt.next  # 先断链
                # 寻找插入位置
                pre1, pre2 = dummy, dummy.next
                while nxt.val > pre2.val:
                    pre1 = pre2
                    pre2 = pre2.next
                # 插入
                pre1.next = nxt
                nxt.next = pre2
                # 再从第一个值开始循环
                nxt = cur.next
        return dummy.next