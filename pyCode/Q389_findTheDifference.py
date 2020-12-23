#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 9:19
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q389_findTheDifference.py
# @Note    : https://leetcode-cn.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
        return t[-1]