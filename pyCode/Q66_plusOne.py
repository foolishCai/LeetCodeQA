#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 8:49
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q66_plusOne.py
# @Note    : https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits[0] = digits[0] + 1
        for idx, num in enumerate(digits):
            if num == 10 and idx<len(digits)-1:
                digits[idx] = 0
                digits[idx+1] = digits[idx+1] + 1
            elif num == 10 and idx==len(digits)-1:
                digits[-1] = 0
                digits.reverse()
                digits = [1] + digits
            elif num < 10 and idx==len(digits)-1:
                digits.reverse()
        return digits





