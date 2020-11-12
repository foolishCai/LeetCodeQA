#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 8:59
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q922_sortArrayByParityII.py
# @Note    : https://leetcode-cn.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j_list = [i for i in A if i%2==1]
        o_list = [i for i in A if i%2==0]
        result_list = []
        for i in range(len(j_list)):
            result_list.append(o_list[i])
            result_list.append(j_list[i])
        return result_list