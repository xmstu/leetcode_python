# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素
        nums = [4,5,6,7,0,1,4]
        nums = [3,3,1,3]
        nums = [1,3,3]
        """
        # 删掉重复元素, 用原来的方法
        s = set() 
        for num in nums[::-1]:
            if num in s:
                nums.remove(num)
                continue
            s.add(num)

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]
 

class Solution2:

    def findMin(self, nums: List[int]) -> int:   
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            # 相等的情况, 不能确定最小值在 mid 的左边还是右边, 但是可以确定的是 right 可以 左移 一位
            else:
                right -= 1
        
        return nums[right]


class TestFindMin:

    """
    pytest -s 154_find_minimum_in_rotated_sorted_array_2.py::TestFindMin
    """

    def test(self):
        solution = Solution2()

        nums = [1,3,5]
        assert 1 == solution.findMin(nums)

        nums = [2,2,2,0,1]
        assert 0 == solution.findMin(nums)

        nums = [4,5,6,7,0,1,4]
        assert 0 == solution.findMin(nums)

        nums = [3,3,1,3]
        assert 1 == solution.findMin(nums)

        nums = [1,3,3]
        assert 1 == solution.findMin(nums)

        nums = [1,1]
        assert 1 == solution.findMin(nums)

        nums = [1,1,1]
        assert 1 == solution.findMin(nums)

