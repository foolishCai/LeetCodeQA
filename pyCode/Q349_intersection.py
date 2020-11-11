# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/2 10:21
# @Author : Cai
# @Email : chenyuwei_0303@yeah.net
# @File : Q349_intersection.py
# @Note : https://leetcode-cn.com/problems/intersection-of-two-arrays/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))