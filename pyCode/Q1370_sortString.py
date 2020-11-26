#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 9:41
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1370_sortString.py
# @Note    : https://leetcode-cn.com/problems/increasing-decreasing-string/

import collections

class Solution:
    def sortString(self, s: str) -> str:
        chars=collections.Counter(s)
        ans=[]
        signal=0
        while chars:
            group=list(chars)
            group.sort(reverse=signal)
            ans.extend(group)
            chars-=collections.Counter(group)
            signal=1-signal
        return ''.join(ans)