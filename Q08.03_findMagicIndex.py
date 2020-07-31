#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 11:34
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q08.03_findMagicIndex.py
# @Note    : https://leetcode-cn.com/problems/magic-index-lcci/


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for idx, value in enumerate(nums):
            if idx == value:
                return idx
        return -1