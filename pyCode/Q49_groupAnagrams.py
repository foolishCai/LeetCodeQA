#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 8:44
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q49_groupAnagrams.py
# @Note    : https://leetcode-cn.com/problems/group-anagrams/


import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            mp[key].append(s)

        return list(mp.values())
