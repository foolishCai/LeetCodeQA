#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 10:11
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q9_isPalindrome.py
# @Note    :

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
