#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 21:27
# @Author  : chenyuwei_0303@yeah.net
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q13_robot_moving.py
# @url     : https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

class Solution:

    def movingCount(self, threshold, rows, cols):  # threshold阈值，count格子数
        # write code here
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        markmatrix = [False] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, markmatrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, markmatrix):
        value = 0
        if self.check(threshold, rows, cols, row, col, markmatrix):
            markmatrix[row * cols + col] = True
            value = 1 + self.movingCountCore(threshold, rows, cols, row - 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row + 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col - 1, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, markmatrix)
        return value

    def check(self, threshold, rows, cols, row, col, markmatrix):  # 满足要求返回True，否则False
        if row >= 0 and row < rows and col >= 0 and col < cols and self.getDigitNum(row) + self.getDigitNum(col) <= threshold and not markmatrix[row * cols + col]:
            return True
        return False

    def getDigitNum(self, number):  # 目的求数位和
        sum = 0
        while (number > 0):
            sum += number % 10
            number = number // 10
        return sum

