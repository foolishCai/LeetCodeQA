#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 8:47
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q135_candy.py
# @Note    : https://leetcode-cn.com/problems/candy/


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count