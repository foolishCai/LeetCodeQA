#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 9:00
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q88_merge.py
# @Note    : https://leetcode-cn.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1