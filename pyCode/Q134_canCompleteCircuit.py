#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 9:11
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q134_canCompleteCircuit.py
# @Note    : https://leetcode-cn.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i]-cost[i] >= 0:
                fuel += gas[i]-cost[i]
            else:
                fuel = 0
                start = i + 1
        for i in range(start):
            if fuel + gas[i]-cost[i] >= 0:
                fuel += gas[i]-cost[i]
            else:
                return -1
        return start