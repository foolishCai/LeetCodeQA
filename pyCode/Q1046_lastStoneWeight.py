#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q1046_lastStoneWeight.py
# @Note    :


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        flg = len(stones)
        while flg > 1:
            stones.sort()
            a, b =stones[-1], stones[-2]
            if a == b:
                stones = stones[:-2]
                flg = flg - 2
            elif a>b:
                stones = stones[:-2]
                stones.append(a-b)
                flg = flg - 1
        if len(stones) == 0:
            return 0
        else:
            return stones[0]