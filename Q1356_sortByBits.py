#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 9:11
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Site    : 
# @File    : Q1356_sortByBits.py
# @Note    : https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'),x))

