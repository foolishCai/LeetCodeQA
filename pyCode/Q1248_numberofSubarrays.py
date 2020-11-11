#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 09:35
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q1248_numberofSubarrays.py
# @Note    : https://leetcode-cn.com/problems/count-number-of-nice-subarrays/


class Solution:
    def numberOfSubarrays(self, nums, k):
        res, cur_sum = 0, 0
        sum_dict = {0: 1}
        for num in nums:
            cur_sum += num & 1
            if cur_sum - k in sum_dict:
                res += sum_dict[cur_sum - k]
            sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1
        print(sum_dict)
        return res