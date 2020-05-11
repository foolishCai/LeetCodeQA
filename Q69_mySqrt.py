#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 09:50
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q69_mySqrt.py
# @Note    : https://leetcode-cn.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right-left)//2
            mid_square = mid**2
            if mid_square == x:
                return mid
            elif mid_square > x:
                right = mid - 1
            else:
                left = mid + 1
        return  min(left, right)