#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 11:29
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q136_singleNumber.py
# @Note    : https://leetcode-cn.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        import collections
        obj = collections.Counter(nums)
        return [k for k, v in obj.items() if v == 1][0]
