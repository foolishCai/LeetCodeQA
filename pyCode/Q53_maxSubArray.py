#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 13:51
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q53_maxSubArray.py
# @Note    : https://leetcode-cn.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre, max_value = 0, min(nums)
        for i in range(len(nums)):
            pre = max(nums[i], pre+nums[i])
            max_value = max(max_value, pre)
        return max_value