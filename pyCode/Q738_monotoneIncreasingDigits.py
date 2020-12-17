#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 8:38
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q738_monotoneIncreasingDigits.py
# @Note    : https://leetcode-cn.com/problems/monotone-increasing-digits/

class Solution:
    def monotoneIncreasingDigits(self,N):
        lst = [int(x) for x in str(N)]
        if len(lst) == 1:
            return N - 1
        max_ = 0
        rs = lst[0]
        count = 0
        for _ in range(len(lst) - 1):
            if (lst[_] < lst[_ + 1])&(lst[_ + 1] >= max_):
                max_ = lst[_ + 1]
                rs *= 10
                rs += lst[_+1]
                count = 0
            elif (lst[_] == lst[_ + 1])&(lst[_ + 1] >= max_):
                rs *= 10
                rs += lst[_+1]
                count += 1
            else:
                print(count)
                print(rs)
                return (rs // 10**count) * 10 ** (len(lst) - _ + count - 1) - 1
        return N



