#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 9:21
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q989_addToArrayForm.py
# @Note    :

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(str(int("".join([str(i)for i in A])) + K))
