# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中 「优美子数组」 的数目。

    思路:
        奇数看作 1, 偶数看作 0, 求前缀和数组 S
        连续子数组 [l,r] 中的奇数个数为 S[r] - S[l-1]

        枚举右端点i, 只需要找到 i 前面有多少个 j 满足 S[i] - S[j] = k
        这其实是两数之差的问题

        所以只需要用一个计数数组或 hash map 维护 S 中每个值的个数
        枚举右端点 i, 看一下等于 S[i] - k 的值有几个就行
    """
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n+1)
        for i in range(1, n+1):
            s[i] = s[i-1] + nums[i-1] % 2
        
        count = [0] * (n+1)
        ans = 0
        count[s[0]] += 1
        for i in range(1, n+1):
            if s[i] - k >= 0:
                ans += count[s[i] - k]
            count[s[i]] += 1

        return ans


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

