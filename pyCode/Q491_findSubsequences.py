#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 19:14
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q491_findSubsequences.py
# @Note    :

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0], )}
        for i in nums[1:]:
            pres.update({j+(i, ) for j in pres if j[-1] <= i})
            pres.add((i, ))
        return [list(i) for i in pres if len(i) > 1]

