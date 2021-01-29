#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 8:44
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q771_numJewelsInStones.py
# @Note    :

import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = dict(collections.Counter(stones))
        return sum([v for k,v in c.items() if k in jewels])