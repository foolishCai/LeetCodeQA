#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q164_maximumGap.py
# @Note    : https://leetcode-cn.com/problems/maximum-gap/


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nn = len(nums)

        if nn < 2:
            return 0

        resultfinal = 0
        sorted_nums = sorted(nums)
        for i in range(nn-1):
            result = sorted_nums[i+1]-sorted_nums[i]
            if result > resultfinal:
                resultfinal = result
        return resultfinal