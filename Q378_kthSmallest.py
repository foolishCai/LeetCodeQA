#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 19:41
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q378_kthSmallest.py
# @Note    : https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[]
        for _ in matrix:
            lst+=_
        return sorted(lst)[k-1]