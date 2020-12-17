#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 14:29
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q714_maxProfit.py
# @Note    : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]
