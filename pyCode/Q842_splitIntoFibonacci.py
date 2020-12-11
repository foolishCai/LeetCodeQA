#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 9:40
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q842_splitIntoFibonacci.py
# @Note    : https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(cur, temp_state):
            if len(temp_state) >= 3 and cur == n:  # 退出条件
                self.res = temp_state
                return
            if cur == n:  # 剪枝
                return
            for i in range(cur, n):
                if S[cur] == "0" and i > cur:  # 当数字以0开头时,应该跳过
                    return
                if int(S[cur: i+1]) > 2 ** 31 - 1 or int(S[cur: i+1]) < 0:  # 剪枝
                    continue
                if len(temp_state) < 2:
                    backtrack(i+1, temp_state + [int(S[cur: i+1])])
                else:
                    if int(S[cur: i+1]) == temp_state[-1] + temp_state[-2]:
                        backtrack(i+1, temp_state + [int(S[cur: i+1])])

        n = len(S)
        self.res = []
        backtrack(0, [])
        return self.res
