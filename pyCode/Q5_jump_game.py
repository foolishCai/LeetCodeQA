#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 14:09
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q5_jump_game.py
# @Note    : https://leetcode-cn.com/problems/jump-game/


class Solution:
    def canJump(self, nums):
        length = len(nums)
        anagy = 0
        for i in range(0, length):
            anagy = max(anagy - 1, nums[i])
            if anagy <= 0 and i < length - 1:
                return False
        return True