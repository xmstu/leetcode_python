# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
    设计一个算法使得这 m 个子数组各自和的最大值最小。

    简化问题: 能否将 nums 分成 m 个连续子数组, 每组的和 <= T
    """
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = 0, 0
        # left 是数组中的最大值, right 是数组的所有数的和, 这样可以保证盒子的大小可以装数组中的最大值
        for num in nums:
            left = max(left, num)
            right += num
        while left < right:
            mid = left + (right - left) // 2
            if self.validate(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        
        return right
    
    def validate(self, nums: List[int], m: int, size: int) -> bool:
        # 计算每个盒子装的数的和
        box = 0
        # 计算盒子的数量
        count = 1
        for num in nums:
            # box 还没装满, 就继续加, 直到加到大于或等于 盒子 size 大小限制
            if box + num <= size:
                box += num
            else:
                count += 1
                box = num
        
        return count <= m



class TestSplitArray:

    """
    pytest -s 410_split_array_largest_sum.py::TestSplitArray
    """

    def test(self):
        solution = Solution()

        nums = [7,2,5,10,8]; m = 2
        assert 18 == solution.splitArray(nums, m)

        nums = [1,2,3,4,5]; m = 2
        assert 9 == solution.splitArray(nums, m)

        nums = [1,4,4]; m = 3
        assert 4 == solution.splitArray(nums, m)
