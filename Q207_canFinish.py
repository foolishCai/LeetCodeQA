#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:16
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q207_canFinish.py
# @Note    : https://leetcode-cn.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or numCourses == 1:
            return True
        graph = dict()
        for i in range(numCourses):
            graph[i] = set()
        for pre in prerequisites:
            graph[pre[0]].add(pre[1])
        to_removed = {n for n, adjs in graph.items() if len(adjs) == 0}
        while to_removed:
            for n in to_removed:
                del graph[n]
            tmp = set()
            for n, adjs in list(graph.items()):
                graph[n] = adjs - to_removed
                if len(graph[n]) == 0:
                    tmp.add(n)
            to_removed = tmp
        return len(graph) == 0