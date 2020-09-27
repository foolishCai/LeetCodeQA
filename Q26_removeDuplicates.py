#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 19:18
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q26_removeDuplicates.py
# @Note    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        while i < l-1:
            if nums[i] == nums[i+1]:
                l = l - 1
                nums.pop(i)
                continue
            i = i +1
        return len(nums)