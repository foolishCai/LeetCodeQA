#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 09:54
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q657_judgeCircle.py
# @Note    : https://leetcode-cn.com/problems/robot-return-to-origin/

class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
