#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 09:44
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q20_isValid.py
# @Note    : https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack