#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 9:13
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q649_predictPartyVictory.py
# @Note    : https://leetcode-cn.com/problems/dota2-senate/

import collections

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"

