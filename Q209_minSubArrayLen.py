#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 19:24
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q209_minSubArrayLen.py
# @Note    : https://leetcode-cn.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        j = 0
        min_len = float("inf")
        while j < length:
            if sum(nums[i:j + 1]) < s:
                j += 1
                continue
            if j - i < min_len:
                min_len = j - i + 1
            i += 1
        return 0 if len(nums) < min_len else min_len