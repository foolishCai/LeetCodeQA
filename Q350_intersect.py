#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 14:30
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q350_intersect.py
# @Note    : https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        result = []
        for n in nums2:
            if n in c and c[n] > 0:
                c[n] -= 1
                result.append(n)
        return result
