#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 10:21
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q43_multiply.py
# @Note    : https://leetcode-cn.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return (str(eval(num1 + '*' + num2)))