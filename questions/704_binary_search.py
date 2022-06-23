# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


class TestSearch:

    """
    pytest -s 704_binary_search.py::TestSearch
    """

    def test(self):
        solution = Solution()

        nums = [-1,0,3,5,9,12]
        target = 9
        assert 4 == solution.search(nums, target)

        nums = [-1,0,3,5,9,12]
        target = 2
        assert -1 == solution.search(nums, target)
