#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 10:24
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q841_canVisitAllRooms.py
# @Note    : https://leetcode-cn.com/problems/keys-and-rooms/


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        st = set()

        def dfs(n: int) -> None:
            if n in st:
                return
            st.add(n)
            for i in rooms[n]:
                dfs(i)

        dfs(0)
        return len(rooms) == len(st)