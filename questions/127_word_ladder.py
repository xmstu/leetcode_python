# -*- coding:utf-8 -*-
from collections import defaultdict, deque
from typing import List


class Solution:
    """
    字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk:

    每一对相邻的单词只差一个字母。
    对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
    sk == endWord
    给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        思路:
            单向bfs, 将beginWord每个位置的字符从 a 到 z 变一次(除字符本身), 判断是否在 wordset, 在的深度加一, 加入队列, 直到和最终字符相等
        """
        wordSet = set()
        depth = defaultdict(int)
        q = deque()

        for s in wordList:
            wordSet.add(s)
        
        if endWord not in wordSet:
            return 0
        
        depth[beginWord] = 1
        q.appendleft(beginWord)
        while q:
            s = q.pop()
            for i in range(len(s)):
                for ch_ord in range(ord('a'), ord('z') + 1):
                    ch = chr(ch_ord)
                    if ch == s[i]:
                        continue
                    ns = s[:i] + ch + s[i+1:]
                    if ns not in wordSet:
                        continue
                    if depth[ns] != 0:
                        continue
                    depth[ns] = depth[s] + 1
                    q.appendleft(ns)
                    if ns == endWord:
                        return depth[ns]
        
        return 0


class Solution2:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set()
        depthBegin = defaultdict(int)
        depthEnd = defaultdict(int)
        qBegin = deque()
        qEnd = deque()

        for s in wordList:
            wordSet.add(s)
        
        if endWord not in wordSet:
            return 0
        
        depthBegin[beginWord] = 1
        depthEnd[endWord] = 1
        qBegin.appendleft(beginWord)
        qEnd.appendleft(endWord)

        def expand(q: deque, depth: dict, depthOther: dict):
            if not q:
                return -1
            while q:
                s = q.pop()
                for i in range(len(s)):
                    for ch_ord in range(ord('a'), ord('z') + 1):
                        ch = chr(ch_ord)
                        if ch == s[i]:
                            continue
                        ns = s[:i] + ch + s[i+1:]
                        if ns not in wordSet:
                            continue
                        if depth[ns] != 0:
                            continue
                        # 双向 Bfs 提前相遇, 返回两边 bfs 的层数之和
                        if depthOther[ns] != 0:
                            return depth[s] + depthOther[ns]
                        depth[ns] = depth[s] + 1
                        q.appendleft(ns)
            
            return -1
        
        while qBegin or qEnd:
            res = expand(qBegin, depthBegin, depthEnd)
            if res != -1:
                return res
            res = expand(qEnd, depthEnd, depthEnd)
            if res != -1:
                return res
        
        return 0



class TestLadderLength:

    """
    pytest -s 127_word_ladder.py::TestLadderLength
    """

    def test(self):
        solution = Solution2()

        beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log","cog"]
        assert 5 == solution.ladderLength(beginWord, endWord, wordList)

        beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log"]
        assert 0 == solution.ladderLength(beginWord, endWord, wordList)
