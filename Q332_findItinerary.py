#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 09:33
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q332_findItinerary.py
# @Note    : https://leetcode-cn.com/problems/reconstruct-itinerary/

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    G = collections.defaultdict(list)  # graph
    for f, t in sorted(tickets, reverse=True):
        G[f] += t,

    def dfs(k):  # DFS
        while G[k]:
            dfs(G[k].pop())
        res.append(k)

    res = []
    dfs('JFK')
    return res