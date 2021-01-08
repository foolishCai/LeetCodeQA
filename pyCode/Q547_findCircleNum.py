#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 8:59
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q547_findCircleNum.py
# @Note    :

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        father = [i for i in range(n)]
        size = [1]*n
        self.count = n
        def find(x):
        # 路径压缩
            while x != father[x]:
                father[x] = find(father[x])
                x = father[x]
            return father[x]

        def union(x, y):
            father_x, father_y = find(x), find(y)
            if father_x == father_y:
                return
            if size[father_x] > size[father_y]:
                father_x, father_y = father_y, father_x
            # father_y的size更大，按秩合并，把小树合并到大树上
            father[father_x] = father_y
            size[father_y] += size[father_x]
            self.count -= 1

        for i in range(n):
            for j in range(i):
                if M[i][j]==1:
                    union(i,j)
        return self.count
