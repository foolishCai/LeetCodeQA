#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 09:21
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q167_twoSum.py
# @Note    : https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for inx, i in enumerate(numbers):
            if i in dct:
                return [dct[i]+1, inx+1]
            dct[target-i] = inx
