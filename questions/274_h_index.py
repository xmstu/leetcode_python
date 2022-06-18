# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    根据维基百科上 h 指数的定义：h 代表“高引用次数”，
    一名科研人员的 h指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
    且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。
    """
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0; i = 0; n = len(citations)
        while i < n and sorted_citation[i] > h:
            print("sorted_citation[i]: %s, i: %s, h: %s" % (sorted_citation[i], i, h))
            h += 1
            i += 1
            print("i: %s, h: %s" % (i, h))
        return h


class TestHIndex:

    """
    pytest -s 274_h_index.py::TestHIndex
    """

    def test(self):
        solution = Solution()

        citations = [3,0,6,1,5]
        assert 3 == solution.hIndex(citations)

        citations = [1,3,1]
        assert 1 == solution.hIndex(citations)
