# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
    区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

    输入: nums = [-2,5,-1], lower = -2, upper = 2,
    输出: 3

    解释: 
        i=0: 
            元素个数逐次递增迭代有以下子数组[-2,],[-2,5],[-2,5,-1]
            对应元素和为-2,3,2,其中-2和2落在范围区间[lower = -2, upper = 2]之间
            因此元素索引区间[0,0],[0,2]符合要求(注意是元素索引区间)
        i=1:
            有子数组[5],[5,-1], 这两个子数组的区间和, 一个是 5, 一个是 4, 都超出范围区间, 不满足
        i=2:
            有子数组[-1], -1 在 [-2:2] 内
        最终得到符合要求的元素索引区间为[0,0],[0,2],[2,2].
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
