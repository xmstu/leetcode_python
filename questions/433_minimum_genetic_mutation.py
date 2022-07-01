# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:
    """
    广度优先搜索模板题
    求最小代价, 最少步数的题目, 用BFS
    BFS是按层次序搜索, 第 K 步搜完才会搜 K + 1 步, 在任意时刻队列中至多只有两层
    """
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        hashBank = {}
        depth = {}
        depth[start] = 0
        for seq in bank:
            hashBank[seq] = True
        if end not in hashBank:
            return -1
        q = deque()
        q.appendleft(start)
        gene = ['A', 'C', 'G', 'T']
        while q:
            s = q.pop()
            for i in range(0, 8):
                for j in range(0, 4):
                    if s[i] != gene[j]:
                        ns = s[:i] + gene[j] + s[i+1:]
                        if ns not in hashBank:
                            continue
                        # 每个点只需要访问一次, 第一次就是最少层数
                        if ns in depth:
                            continue
                        depth[ns] = depth[s] + 1
                        q.appendleft(ns)
                        if ns == end:
                            return depth[ns]
        return -1


class TestMinMutation:

    """
    pytest -s 433_minimum_genetic_mutation.py::TestMinMutation
    """

    def test(self):
        solution = Solution()

        start = "AACCGGTT"; end = "AACCGGTA"; bank = ["AACCGGTA"]
        assert 1 == solution.minMutation(start, end, bank)
        
        start = "AACCGGTT"; end = "AAACGGTA"; bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        assert 2 == solution.minMutation(start, end, bank)

        start = "AAAAACCC"; end = "AACCCCCC"; bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
        assert 3 == solution.minMutation(start, end, bank)

