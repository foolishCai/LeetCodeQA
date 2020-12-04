#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 9:07
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q34_searchRange.py
# @Note    : https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums, low, high, x):
            if low > high:return
            mid = low + (high-low)//2
            ans = [-1,-1]
            if nums[mid] == x:
                left = binarysearch(nums, low, mid-1,x) # 左侧
                right = binarysearch(nums, mid+1, high,x) # 右侧
                if left:
                    ans[0] = left[0]
                    ans[1] = mid
                else:ans[0] = mid
                if right: ans[1] = right[1]
                else: ans[1] = mid
                return ans
            else:
                if nums[mid] < x: return binarysearch(nums, mid+1,high,x)
                else: return binarysearch(nums, low, mid-1, x)
        res = binarysearch(nums, 0, len(nums)-1, target)
        return res if res else [-1,-1]
