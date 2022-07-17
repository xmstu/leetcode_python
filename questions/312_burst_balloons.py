# -*- coding:utf-8 -*-
from copy import deepcopy
from typing import List


class Solution:

    """
    有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
    求所能获得硬币的最大数量。

    思路:
        最后一个戳的是哪个气球
        先戳完 [l, p - 1] 和 [p + 1, r], 最后戳 p
        子问题两端相邻的气球不变, 只有区间端点是变化信息
        满足同类子问题

        转移方程:
            f[l,r]表示戳破闭区间 l~r 之间的所有气球, 所获硬币最大数量
            决策: 最后一个戳的是p
                f[l,r] = max(f[l,p-1] + f[p+1,r] + nums[p] * nums[l-1] * nums[r+1])
            初值: l > r时, f[l,r] = 0
            目标: f[1,n]
    """
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        f = [[0] * (n+2) for _ in range(n+2)]
        for length in range(1, n+1):
            for l in range(1, n - length + 1 + 1):
                r = l + length - 1
                for p in range(l, r+1):
                    f[l][r] = max(f[l][r], f[l][p-1] + f[p+1][r] + nums[p] * nums[l-1] * nums[r+1])
        return f[1][n]


class Solution2:

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = deepcopy(nums)
        nums1.insert(0, 1)
        nums1.append(1)
        f = [[-1] * (n+1) for _ in range(n+1)]

        def calc(l: int, r: int):
            if l > r:
                return 0
            if f[l][r] != -1:
                return f[l][r]
            for p in range(l, r+1):
                f[l][r] = max(f[l][r], calc(l, p - 1) + calc(p + 1, r) + nums1[p] * nums1[l - 1] * nums1[r + 1])
            
            return f[l][r]

        return calc(1, n)


class TestMaxCoins:

    """
    pytest -s 312_burst_balloons.py::TestMaxCoins
    """

    def test(self):
        solution = Solution2()

        nums = [3,1,5,8]
        assert 167 == solution.maxCoins(nums)

        nums = [1,5]
        assert 10 == solution.maxCoins(nums)
