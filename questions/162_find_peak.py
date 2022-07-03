# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    三分查找经典题

    峰值元素是指其值严格大于左右相邻值的元素。
    给你一个整数数组 nums, 找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞ 。
    你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
    """
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            # lmid 取中值, rmid 比 lmid 多加一位即可, 就可以判断这两个数是递增还是递减
            lmid = left + (right - left) // 2
            rmid = lmid + 1
            # 递增, left = lmid + 1
            if nums[lmid] <= nums[rmid]:
                left = lmid + 1
            # 递减, right = rmid - 1
            else:
                right = rmid - 1
        
        return right


class TestFindPeakElement:

    """
    pytest -s 162_find_peak.py::TestFindPeakElement
    """

    def test(self):
        solution = Solution()

        nums = [1,2,3,1]
        assert 2 == solution.findPeakElement(nums)

        nums = [1,2,1,3,5,6,4]
        assert 5 == solution.findPeakElement(nums)
