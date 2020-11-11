#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 09:28
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q347_topKFrequent.py
# @Note    :


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        s = dict(Counter(nums))
        s = sorted(s.items(), key=lambda item: item[1], reverse=True)
        return [s[i][0] for i in range(k)]