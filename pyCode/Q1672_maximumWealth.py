#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 19:36
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1672_maximumWealth.py
# @Note    :

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])