#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 8:57
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q27_removeElement.py
# @Note    : https://leetcode-cn.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)

