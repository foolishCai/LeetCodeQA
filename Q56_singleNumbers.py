#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 16:17
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q56_singleNumbers.py
# @Note    : https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/


import collections
class Solution:
    def singleNumbers(self, nums):
        c = collections.Counter(nums)
        result = [k for k, v in c.items() if v == 1]
        return result