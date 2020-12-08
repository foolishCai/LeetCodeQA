#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 8:49
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q861_matrixScore.py
# @Note    : https://leetcode-cn.com/problems/score-after-flipping-matrix/


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 先把行数和列数算出来
        m,n = len(A), len(A[0])

        # result是最后要的结果，先定为0
        result = 0

        for j in range(1, n):
            # 第j列的和，先定为0
            j_sum = 0
            for i in range(m):
                # 如果行首为1，不反转，保持原样，加入到j_sum
                if A[i][0] == 1:
                    j_sum += A[i][j]
                # 如果行首为0，该行需要翻转，然后加入到j_sun
                else:
                    j_sum += 1 - A[i][j]
            # 算出行翻转后，该列的和为j_sum
            # 此时考虑j要不要列翻转。翻转后，第j列的和为m-j_sum。比较一下大小即可
            j_result = max(j_sum, m - j_sum)

            # 把第j列的结果加入到总结果中，第j列每一个1，实际值为2**(n-j-1)
            result += j_result * 2 ** (n - j - 1)
        # 最后把第一列，全是1的结果，加入到总结果中
        result += 2 ** (n - 1) * m
        return result

