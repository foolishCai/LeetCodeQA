#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 9:03
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q455_findContentChildren.py
# @Note    :

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count
