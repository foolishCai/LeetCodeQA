#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 13:47
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q343_integerBreak.py
# @Note    : https://leetcode-cn.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        ans=0
        #拆分成i份
        for i in range(2,n+1):
            #每份的份额为share
            share=n//i
            #总共多余的部分extra
            extra=n%i
            #有extra份额外加1，剩下的i-extra份仍然保持原有份额share
            tmp=(share+1)**extra*share**(i-extra)
            ans=max(ans,tmp)
        return ans
