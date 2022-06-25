# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    给你一个按照非递减顺序排列的整数数组 nums, 和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target, 返回 [-1, -1]。
    你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # 先找后继
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        ans.append(right)
        # 再找前驱
        left, right = -1, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        ans.append(right)
        
        if ans[0] > ans[1]:
            return [-1, -1]

        return ans


class TestSearchRange:

    """
    pytest -s 34_find_first_and_last_position_of_element_in_sorted_array.py::TestSearchRange
    """

    def test(self):
        solution = Solution()

        nums = [5,7,7,8,8,10]
        target = 8
        assert [3,4] == solution.searchRange(nums, target)

        nums = [5,7,7,8,8,10]
        target = 6
        assert [-1,-1] == solution.searchRange(nums, target)

        nums = []
        target = 0
        assert [-1,-1] == solution.searchRange(nums, target)
