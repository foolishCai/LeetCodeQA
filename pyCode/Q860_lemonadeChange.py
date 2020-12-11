#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 8:51
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q860_lemonadeChange.py
# @Note    : https://leetcode-cn.com/problems/lemonade-change/


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        from collections import defaultdict
        if bills and (bills[0] == 10 or bills[0] == 20):
            return False

        res = defaultdict(int)
        for x in bills:
            if x == 10:
                if res[5] >= 1:
                    res[5] -= 1
                else:
                    return False
            if x == 20:
                if res[10] >= 1 and res[5] >= 1:
                    res[10] -= 1
                    res[5] -= 1
                    continue
                if res[5] >= 3:
                    res[5] -= 3
                    continue
                else:
                    return False
            res[x] += 1
        return True
