#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 10:02
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q29_spiralOrder.py
# @Note    : https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            tmp = [matrix[top][column] for column in range(left, right+1)]
            order.extend(tmp)

            tmp = [matrix[row][right] for row in range(top + 1, bottom + 1)]
            order.extend(tmp)

            if left < right and top < bottom:
                tmp = [matrix[bottom][column] for column in range(right - 1, left, -1)]
                order.extend(tmp)
                tmp = [matrix[row][left] for row in range(bottom, top, -1)]
                order.extend(tmp)

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
