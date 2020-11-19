#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 8:47
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q283_move-zeroes.py
# @Note    : https://leetcode-cn.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)  #原始数组长度
        while True:   #删除数组中的所有0
            try:
                nums.remove(0)
            except:
                break
        nums += [0]*(l-len(nums)) #数组长度减少的就是删除的0的个数
        return nums
