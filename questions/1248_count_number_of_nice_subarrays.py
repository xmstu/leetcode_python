# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中 「优美子数组」 的数目。
    """
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pass


class TestNumberOfSubarrays:

    """
    pytest -s 1248_count_number_of_nice_subarrays.py::TestNumberOfSubarrays
    """

    def test(self):
        solution = Solution()

        nums = [1,1,2,1,1]; k = 3
        assert 2 == solution.numberOfSubarrays(nums, k)

        nums = [2,4,6]; k = 1
        assert 0 == solution.numberOfSubarrays(nums, k)

        nums = [2,2,2,1,2,2,1,2,2,2]; k = 2
        assert 16 == solution.numberOfSubarrays(nums, k)

