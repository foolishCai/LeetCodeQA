#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 20:25
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q20_isNumber.py
# @Note    : https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False