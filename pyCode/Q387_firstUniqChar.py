#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 8:52
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q387_firstUniqChar.py
# @Note    : https://leetcode-cn.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ss = Counter(s)
        ss = [s.index(k) for k,v in ss.items() if v==1]
        if ss:
            return min(ss)
        else:
            return -1
