#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 15:49
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q40_combinationSum2.py
# @Note    : https://leetcode-cn.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0 or len(candidates) == 0:
            return []
        result = []

        def helper(tar, idx, cur):
            if tar == 0:  # 终止条件
                result.append(cur[:])
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                # 下面调用helper时，第二个参数的位置是i+1，一定是从当前一位的下一位开始找(开始的时候写成了idx，一直无法减枝)
                helper(tar - candidates[i], i + 1, cur)
                cur.pop()  # 回溯记得恢复状态

        candidates.sort()
        helper(target, 0, [])
        return result
