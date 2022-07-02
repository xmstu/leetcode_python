# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
    区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

    意思是给你个lower，upper上下限，让你从目标数组arr里找各种可能的子数组满足子数组的sum求和在给定上下限之内
    """
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pass


class TestCountRangeSum:

    """
    pytest -s 327_count_range_sum.py::TestCountRangeSum
    """

    def test(self):
        solution = Solution()

        nums = [-2,5,-1]; lower = -2; upper = 2
        assert 3 == solution.countRangeSum(nums, lower, upper)

        nums = [0]; lower = 0; upper = 0
        assert 1 == solution.countRangeSum(nums, lower, upper)
