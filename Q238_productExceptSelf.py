#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 10:02
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q238_productExceptSelf.py
# @Note    : https://leetcode-cn.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(l[i] * r[i])
        return res
