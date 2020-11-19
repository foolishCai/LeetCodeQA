#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 9:03
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q406_reconstructQueue.py
# @Note    : https://leetcode-cn.com/problems/queue-reconstruction-by-height/


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1:
            return people

        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]
        for i in people[1:]:
            new_people.insert(i[1], i)
        return  new_people