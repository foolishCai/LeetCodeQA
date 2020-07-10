#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 14:48
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q215_findKthLargest.py
# @Note    : https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

from heapq import heappush, heapreplace, nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]