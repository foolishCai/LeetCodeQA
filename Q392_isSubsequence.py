#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 09:31
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q392_isSubsequence.py
# @Note    :

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        for i in t:
            if s[0] == i:
                s = s[1:]
            if not s:
                return True
        return False
