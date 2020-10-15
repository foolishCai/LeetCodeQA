#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 16:11
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q58_lengthOfLastWord.py
# @Note    :

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ll = s.split(" ")
        ll = [i for i in ll if i!=""]
        if len(ll) == 0:
            return 0
        else:
            return len(ll[-1])