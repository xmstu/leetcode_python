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
    def countRangeSumNaive(self, nums: List[int], lower: int, upper: int) -> int:
        """
        朴素解法: 两层 for 循环求子数组的和在不在范围区间内, 在的结果加1
        优点: 代码简单
        缺点: 暴力求解超时
        """

        ans = 0

        for i in range(len(nums)):
            range_sum = nums[i]
            for j in range(i, len(nums)):
                if j > i:
                    range_sum += nums[j]
                if lower <= range_sum <= upper:
                    ans += 1

        return ans

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        归并排序求解
        """
        self.ans = 0
        self.lower = lower
        self.upper = upper
        # 构建前缀和数组
        prefixSumNums = [0 for _ in range(len(nums) + 1)]
        for index, num in enumerate(nums):
            prefixSumNums[index+1] = prefixSumNums[index] + num
        self.mergesort(prefixSumNums, 0, len(prefixSumNums) - 1)
        return self.ans
    
    def mergesort(self, nums: List[int], left: int, right: int):
        # 递归终止条件
        if left >= right:
            return

        # 本层要做的事 
        mid = left + (right - left) // 2
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
    
    def merge(self, nums: List[int], left: int, mid: int, right: int):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        # 计算区间和 满足 [lower:upper] 的个数
        ii, jj, kk = left, mid + 1, mid + 1
        while ii <= mid:
            while jj <= right and nums[jj] - nums[ii] < self.lower:
                jj += 1
            while kk <= right and nums[kk] - nums[ii] <= self.upper:
                kk += 1
            self.ans += (kk - jj)
            ii += 1

        if i <= mid:
            temp += nums[i: mid + 1]
        if j <= right:
            temp += nums[j: right + 1]
        nums[left:right+1] = temp


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

        nums = [0,-3,-3,1,1,2]; lower = 3; upper = 5
        assert 2 == solution.countRangeSum(nums, lower, upper)

        nums = [-3,1,2,-2,2,-1]; lower = -3; upper = -1
        assert 7 == solution.countRangeSum(nums, lower, upper)
