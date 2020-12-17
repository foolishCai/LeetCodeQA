#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 8:40
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q290_wordPattern.py
# @Note    : https://leetcode-cn.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True
