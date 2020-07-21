#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 10:16
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q35_searchInsert.py
# @Note    : https://leetcode-cn.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)