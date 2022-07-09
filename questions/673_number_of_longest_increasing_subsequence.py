# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个未排序的整数数组 nums, 返回最长递增子序列的个数 。
    注意 这个数列必须是 严格 递增的。
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        pass


class TestFindNumberOfLIS:

    def test(self):

        solution = Solution()

        nums = [1,3,5,4,7]
        assert 2 == solution.findNumberOfLIS(nums)

        nums = [2,2,2,2,2]
        assert 5 == solution.findNumberOfLIS(nums)
