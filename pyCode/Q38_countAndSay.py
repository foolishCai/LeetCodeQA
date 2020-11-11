#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 8:48
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q38_countAndSay.py
# @Note    : https://leetcode-cn.com/problems/count-and-say/

import re
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        p = r'(\d)\1*'
        pattern = re.compile(p)
        for _ in range(n - 1):
            print("_ = ", _)
            res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)
            print("res = ", res)
        return res