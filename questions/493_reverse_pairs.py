# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
    你需要返回给定数组中的重要翻转对的数量
    """
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        self.mergesort(nums, 0, len(nums) - 1)
        return self.ans
    
    def mergesort(self, nums, left, right):
        if left >= right:
            return
        
        mid = (left + right) >> 1
        # 计算好左边的翻转对个数, 再算右边的翻转对个数, 最后算跨越左右的翻转对个数
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self.calculate(nums, left, mid, right)
        self.merge(nums, left, mid, right)
    
    def calculate(self, nums, left, mid, right):
        # 左边[left, mid], 右边[mid + 1, right]
        j = mid
        # i 从 left 到 mid, j 从 mid 到 right - 1, 用 nums[left:mid+1] 和 nums[mid+1:right+1] 比较
        for i in range(left, mid + 1):
            while j < right and nums[i] > 2 * nums[j + 1]:
                j += 1
            self.ans += j - mid

    def merge(self, nums, left, mid, right):
        temp = [0 for _ in range(right - left + 1)]
        i = left
        j = mid + 1
        for k in range(len(temp)):
            if j > right or (i <= mid and nums[i] <= nums[j]):
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
        
        nums[left:right+1] = temp


class TestReversePairs:

    """
    pytest -s 493_reverse_pairs.py::TestReversePairs
    """

    def test(self):

        solution = Solution()

        nums = [1,3,2,3,1]
        assert 2 == solution.reversePairs(nums)

        nums = [2,4,3,5,1]
        assert 3 == solution.reversePairs(nums)
