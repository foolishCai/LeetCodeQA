#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:02
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q3_lengthOfLongestSubstring.py
# @Note    : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len