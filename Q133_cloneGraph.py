#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 17:06
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q133_cloneGraph.py
# @Note    : https://leetcode-cn.com/problems/clone-graph

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
