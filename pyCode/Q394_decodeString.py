#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 09:47
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q394_decodeString.py
# @Note    : https://leetcode-cn.com/problems/decode-string/

import re

class Solution:
    def decodeString(self, s:str)->str:
        pattern = re.compile(r'(\d+)\[(\w+)\]')
        m = pattern.findall(s)
        while m:
            for num, char in m:
                s = s.replace(f'{num}[{char}]', char*int(num))
            m = pattern.findall(s)
        return s