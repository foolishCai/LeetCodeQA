#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 09:09
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q125_isPalindrome.py
# @Note    : https://leetcode-cn.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
            elif not s[hi].isalnum():
                hi -= 1
            else:
                if s[lo].lower() == s[hi].lower():
                    lo += 1
                    hi -= 1
                else:
                    return False
        return True