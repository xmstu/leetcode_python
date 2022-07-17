# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        maxDist = 0
        end_index = len(nums)-1
        for i, jump in enumerate(nums):
            if maxDist >= i and i+jump > maxDist:
                maxDist = i + jump
                # 当前最大距离已经大于最大的索引, 可以提前结束
                if maxDist >= end_index:
                    return True
        
        return False


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(0, i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[n-1]


class TestJump:

    """
    pytest -s 55_jump_game.py::TestJump
    """

    def test(self):
        solution = Solution()

        nums = [2,3,1,1,4]
        assert True == solution.canJump(nums)

        nums = [3,2,1,0,4]
        assert False == solution.canJump(nums)
