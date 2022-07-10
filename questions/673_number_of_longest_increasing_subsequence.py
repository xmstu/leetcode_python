# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个未排序的整数数组 nums, 返回最长递增子序列的个数 。
    注意 这个数列必须是 严格 递增的。

    思路
    结合 f[i] 的转移过程，不失一般性地考虑 g[i] 该如何转移：

    同理，由于每个数都能独自一个成为子序列，因此起始必然有 g[i] =1
    枚举区间 [0, i) 的所有数 nums[j]，如果满足 nums[j] < nums[i]，说明 nums[i] 可以接在 nums[j] 后面形成上升子序列，
    这时候对 f[i] 和 f[j] + 1 的大小关系进行分情况讨论：
        1. 满足 f[i] < f[j] + 1: 说明 f[i] 会被 f[j] + 1 直接更新，此时同步直接更新 g[i] = g[j] 即可,
           为什么数量不变? 因为把nums[i]添加到nums[j]的子序列后，最长子序列的数量并没有变化。    
        2. 满足 f[i] = f[j] + 1: 说明找到了一个新的符合条件的前驱, 此时将值继续累加到方案数当中, 即有 g[i] += g[j]。

    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_len, ans = 0, 0
        # 一个记录每个下标对应的最长上升子序列长度
        f = [0] * n
        # 一个记录每个下标对应的最长上升子序列的个数
        g = [0] * n
        for i in range(n):
            f[i] = 1
            g[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1
                        g[i] = g[j]  # 重置计数
                    elif f[j] + 1 == f[i]:
                        g[i] += g[j]
            if f[i] > max_len:
                max_len = f[i]
                ans = g[i]  # 重置计数
            elif f[i] == max_len:
                ans += g[i]

        return ans

class TestFindNumberOfLIS:

    """
    pytest -s 673_number_of_longest_increasing_subsequence.py::TestFindNumberOfLIS
    """

    def test(self):

        solution = Solution()

        nums = [1,3,5,4,7]
        assert 2 == solution.findNumberOfLIS(nums)

        nums = [2,2,2,2,2]
        assert 5 == solution.findNumberOfLIS(nums)

        nums = [1,2,4,3,5,4,7,2]
        assert 3 == solution.findNumberOfLIS(nums)
