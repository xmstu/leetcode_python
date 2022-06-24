# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        3 4 5 1 2 让每个数尝试跟结尾比较 nums[i] <= nums[n-1]
        0 0 0 1 1


        4 5 6 7 0 1 2
        0 0 0 0 1 1 1
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]


class TestFindMin:

    """
    pytest -s 153_find_minimum_in_rotated_sorted_array.py::TestFindMin
    """

    def test(self):
        solution = Solution()

        nums = [3,4,5,1,2]
        assert 1 == solution.findMin(nums)

        nums = [4,5,6,7,0,1,2]
        assert 0 == solution.findMin(nums)

        nums = [11,13,15,17]
        assert 11 == solution.findMin(nums)

