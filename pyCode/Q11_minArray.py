#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 10:16
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q11_minArray.py
# @Note    : https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]
