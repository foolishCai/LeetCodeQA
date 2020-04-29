#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 09:50
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q33_search.py
# @Note    : https://leetcode-cn.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1