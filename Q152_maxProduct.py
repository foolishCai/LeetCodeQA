#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 09:10
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q152_maxProduct.py
# @Note    : https://leetcode-cn.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(1, n + 1):
            temp = a
            a = max(a * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            b = min(temp * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            ans = max(ans, a)
        return ans
