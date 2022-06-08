# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, num in enumerate(nums):
            if target - num in map.keys():
                return [map[target - num], index]
            else:
                map[num] = index
        
        return []


class TestTwoSum:

    """
    pytest -s 1_two_sum.py::TestTwoSum
    """

    def test(self):
        solution = Solution()

        nums = [2,7,11,15]
        target = 9
        assert [0,1] == solution.twoSum(nums, target)

        nums = [3,2,4]
        target = 6
        assert [1,2] == solution.twoSum(nums, target)

        nums = [3,3]
        target = 6
        assert [0,1] == solution.twoSum(nums, target)

