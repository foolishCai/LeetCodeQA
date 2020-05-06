#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:46
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q20_happyNum.py
# @Note    : https://leetcode-cn.com/problems/happy-number/


class Solution:
    def isHappy(self, n):
        sumNum = 0
        while n != 0:
            sumNum += pow((n % 10), 2)
            n //= 10
            if n == 0:
                if sumNum == 1 or sumNum == 7:
                    return True
                if sumNum < 10:
                    return False
                else:
                    n = sumNum
                    sumNum = 0
