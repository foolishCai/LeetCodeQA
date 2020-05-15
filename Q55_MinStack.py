#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 08:39
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q55_MinStack.py
# @Note    : https://leetcode-cn.com/problems/min-stack/


import  math
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
