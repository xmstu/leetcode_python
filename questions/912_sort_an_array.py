# -*- coding:utf-8 -*-
from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        pivot = self.partition(arr, left, right)
        self.quickSort(arr, left, pivot)
        self.quickSort(arr, pivot + 1, right)

    def partition(self, arr, left, right):
        # 随机选中轴
        pivot = random.randint(left, right)
        pivotVal = arr[pivot]

        while left <= right:
            while arr[left] < pivotVal:
                left += 1
            while arr[right] > pivotVal:
                right -= 1
            if left == right:
                break
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return right


class TestSort:

    """
    pytest -s 912_sort_an_array.py::TestSort
    """

    def test(self):
        solution = Solution()

        nums = [5,2,3,1]
        assert [1,2,3,5] == solution.sortArray(nums)

        nums = [5,1,1,2,0,0]
        assert [0,0,1,1,2,5] == solution.sortArray(nums)
