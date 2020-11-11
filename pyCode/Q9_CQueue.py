#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 20:13
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q9_CQueue.py
# @Note    :

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
