# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        for i, num in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[n] = nums[i]
                n += 1
        return n


class TestRemoveDuplicates(object):

    """
    执行命令跑单测:  pytest -s 26_remove_duplicates_from_sorted_array.py::TestRemoveDuplicates
    """

    def test_remove_duplicates(self):
        solution = Solution()
        nums = [1,1,2]
        assert 2 == solution.removeDuplicates(nums)
        nums = [0,0,1,1,1,2,2,3,3,4]
        assert 5 == solution.removeDuplicates(nums)



