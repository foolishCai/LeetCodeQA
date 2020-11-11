#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 09:02
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q459_repeatedSubstringPattern.py
# @Note    : https://leetcode-cn.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
