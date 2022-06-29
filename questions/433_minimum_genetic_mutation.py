# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    广度优先搜索模板题
    """
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        pass


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

