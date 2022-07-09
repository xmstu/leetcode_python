# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    f[i] 表示前 i 个数构成的以 a[i] 为结尾的最长上升子序列的长度
    f[i] = max(f[j] + 1)
    j < i, a[j] < a[i]

    边界: f[i] = 1 (0 <= i < n)
    目标: max(f[i])
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums [j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        
        ans = max(f)
        return ans


class Solution2:
    """
    f[i] 表示前 i 个数构成的以 a[i] 为结尾的最长上升子序列的长度
    f[i] = max(f[j] + 1)
    j < i, a[j] < a[i]

    边界: f[i] = 1 (0 <= i < n)
    目标: max(f[i])
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        记录最长上升子序列的方案
        """
        n = len(nums)
        f = [1] * n
        # 用 pre 数组记录每个 i 是由 哪个 j 的下标转移过来的, 在最后用一个递归函数将答案回溯出来
        pre = [-1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums [j] < nums[i] and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
                    pre[i] = j
        
        ans = 0
        end = -1
        for i in range(0, n):
            if f[i] > ans:
                ans = f[i]
                end = i
        print("pre: %s, end: %s" % (pre, end))
        self.lis = []
        self.get_lis(nums, pre, end)
        print("self.lis: %s" % self.lis)
        return ans
    
    def get_lis(self, nums: List[int], pre: List[int], i):
        if pre[i] != -1:
            self.get_lis(nums, pre, pre[i])
        
        self.lis.append(nums[i])


class TestLengthLIS:

    """
    pytest -s 300_longest_increasing_subsequence.py::TestLengthLIS
    """

    def test(self):

        solution = Solution2()

        nums = [10,9,2,5,3,7,101,18]
        assert 4 == solution.lengthOfLIS(nums)

        nums = [0,1,0,3,2,3]
        assert 4 == solution.lengthOfLIS(nums)

        nums = [7,7,7,7,7,7,7]
        assert 1 == solution.lengthOfLIS(nums)
