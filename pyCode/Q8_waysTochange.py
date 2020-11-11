#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 10:33
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q8_waysTochange.py
# @Note    : https://leetcode-cn.com/problems/coin-lcci/

"""
该问题等价于求方程n = 25a + 10b + 5c + d的非负整数解的数量。
注意到25, 10, 5均为5的倍数，令n = 5m + k, 0 <= k <= 4,
得到：5m = 25a + 10b + 5c + (d-k)
令e = (d-k)/5，显然e必为整数，且与d一一对应。
则原方程解的数量等于mpwd = 5a + 2b + c + e的解的数量, 记为F(m)。

考虑a的取值。

当a = 0时，相当于求方程m = 2b + c + e的非负整数解的数量。
若b = i，则解数为(m - 2i + 1)，因此，此时总的解数是对(m - 2i + 1)从i = 0到[m/2]求和。
（[x]是取下整函数），该和为([m/2] + 1)([(m+1)/2] + 1)；
当a > 0时，有a' = a - 1 >= 0，从而解的数量等于m - 5 = 5a' + 2b + c + e解的数量，即F(m - 5)；
综上，F(m) = F(m - 5) + ([m/2] + 1)([(m+1)/2] + 1)。
"""
class Solution:
    def waysToChange(self, n):
        n = n // 5
        ans = 0
        while n >= 0:
            ans = (ans + (n//2+1)*((n+1)//2+1))
            n -= 5
        return ans % 1000000007