#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 10:08
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q64_atoi.py
# @Note    : https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/


class Solution:
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res