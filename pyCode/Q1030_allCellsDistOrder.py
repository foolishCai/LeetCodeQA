#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 12:41
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1030_allCellsDistOrder.py
# @Note    : https://leetcode-cn.com/problems/matrix-cells-in-distance-order/solution/


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        from functools import cmp_to_key

        def cmp(x, y):
            d1 = abs(x[0] - r0) + abs(x[1] - c0)
            d2 = abs(y[0] - r0) + abs(y[1] - c0)
            return d1 - d2  # 按照曼哈顿距离递增
        matrix = [[r, c] for r in range(R) for c in range(C)]
        matrix = sorted(matrix, key=cmp_to_key(cmp))
        return matrix