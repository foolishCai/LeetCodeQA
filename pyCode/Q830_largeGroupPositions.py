#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 8:59
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q830_largeGroupPositions.py
# @Note    :

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        S = S + '0'  # for loop convenience
        curC = None
        start = 0
        result = []
        for i in range(len(S)):
            if S[i] != curC:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i
                curC = S[i]
        return result

