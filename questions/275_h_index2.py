# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0; right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left


class TestHIndex:

    """
    pytest -s 275_h_index.py::TestHIndex
    """

    def test(self):
        solution = Solution()

        citations = [0,1,3,5,6]
        assert 3 == solution.hIndex(citations)

        citations = [1,2,100]
        assert 2 == solution.hIndex(citations)
