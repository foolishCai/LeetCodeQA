#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 09:33
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q974_subarraysDivByK.py
# @Note    : https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/


# 我们统计以 i 结尾的符合条件的子数组个数。
# 我们可以维护一个以前缀和模 K 的值为键，出现次数为值的哈希表 record
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
            print("elem={}, record={}".format(elem, record))
        return ans

    # 对于两个数 a 和 b，如果有 (a - b) % k == 0，那么 a % k == b % k。
    def subarraysDivByK_v2(self, A: List[int], K: int) -> int:
        from collections import Counter
        from itertools import accumulate
        c = Counter(i % K for i in [0, *accumulate(A)])
        return sum(c[k] * (c[k] - 1) // 2 for k in c)

