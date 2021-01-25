#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 9:13
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q367_isPerfectSquare.py
# @Note    :

import numpy as np
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if float(np.sqrt(num)) == int(np.sqrt(num)):
            return True
        else:
            return False