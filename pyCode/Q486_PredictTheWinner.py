#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 13:18
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q486_PredictTheWinner.py
# @Note    : https://leetcode-cn.com/problems/predict-the-winner/
#
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn)
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)
            return max(scoreStart * turn, scoreEnd * turn) * turn

        return total(0, len(nums) - 1, 1) >= 0