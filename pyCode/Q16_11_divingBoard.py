#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 17:49
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q16_11_divingBoard.py
# @Note    :

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k or k <= 0:
            return []
        elif shorter == longer:
            return [shorter*k]
        else:
            result = [0] * k
            for i in range(k+1):
                result[i] = shorter*(k-i) + longer*i
            return result
