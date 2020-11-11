#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 10:45
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q718_findLength.py
# @Note    : https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/

class Solution:
    def findLength(self, A, B):
        def helper(A,B):
            ans, sizeA, sizeB=0, len(A), len(B)
            for i in range(sizeA):
                tans=0
                for x,y in zip(range(i, sizeA), range(sizeB)):
                    if A[x] == B[y]:
                        tans += 1
                        ans = max(ans, tans)
                    else:
                        tans = 0
            return ans
        return max(helper(A, B), helper(B, A))