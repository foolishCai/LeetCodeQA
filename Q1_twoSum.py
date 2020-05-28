#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 09:57
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q1_twoSum.py
# @Note    : https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x