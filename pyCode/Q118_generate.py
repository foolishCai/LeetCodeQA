#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 8:55
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q118_generate.py
# @Note    :

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            L = [[1], [1, 1]]
            n = 3
            while n <= numRows:
                for i in range(0, n - 1):
                    L.append([])
                    if i == 0:
                        L[n - 1].append(1)
                        L[n - 1].append(1)
                    else:
                        L[n - 1].insert(i, L[n - 2][i] + L[n - 2][i - 1])
                n = n + 1
            return L[:numRows]