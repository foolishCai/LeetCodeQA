#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 09:26
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q1431_kidsWithCandies.py
# @Note    :

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_candies = [i+extraCandies for i in candies]
        result = [all([c>= i for i in candies]) for c in new_candies]
        return result
