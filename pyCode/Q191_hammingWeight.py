#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 9:03
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q191_hammingWeight.py
# @Note    :

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
