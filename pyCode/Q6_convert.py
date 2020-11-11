#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 09:51
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q6_convert.py
# @Note    : https://leetcode-cn.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)