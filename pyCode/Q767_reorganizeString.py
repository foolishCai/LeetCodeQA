#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 9:08
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q767_reorganizeString.py
# @Note    : https://leetcode-cn.com/problems/reorganize-string/solution/

import collections

class Solution:
    def reorganizeString(self, S: str) -> str:
        s = sorted(S)
        count = collections.Counter(S)
        s.sort(key=count.get)
        n = len(s) // 2
        if s[n - 1] == s[-1]:
            return ''

        a, b = s[:n], s[n:]
        for i in range(len(b)):
            s[i * 2] = b[i]
        for i in range(len(a)):
            s[i * 2 + 1] = a[i]

        return ''.join(s)
