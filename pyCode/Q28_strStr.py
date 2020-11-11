#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 9:23
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q28_strStr.py
# @Note    : https://leetcode-cn.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
