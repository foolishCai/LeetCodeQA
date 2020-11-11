#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 09:48
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q287_findDuplicate.py
# @Note    : https://leetcode-cn.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_count = [0] * (len(nums)-1)
        for i in nums:
            nums_count[i-1] += 1
            if nums_count[i-1] > 1:
                return i