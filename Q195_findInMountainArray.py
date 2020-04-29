#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 09:35
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q195_findInMountainArray.py
# @Note    : https://leetcode-cn.com/problems/find-in-mountain-array/

# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        # 找到山峰
        left, right = 0, mountain_arr.length() - 1
        mount_idx = 0
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            midl_val = mountain_arr.get(mid - 1)
            midr_val = mountain_arr.get(mid + 1)
            if midl_val < mid_val and mid_val > midr_val:
                mount_idx = mid
                break
            if midl_val < midr_val:
                left = mid
            else:
                right = mid
        # 尝试在山峰左侧（递增区间）能否找到target
        left, right = 0, mount_idx
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid  # 如果在该循环找不到，也就不会返回，就会进入到右侧递减区间的查找
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        # 尝试在山峰右侧（递减区间）能否找到target
        left, right = mount_idx, mountain_arr.length() - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # 如果在右侧递减区间也没能找到，则返回-1
