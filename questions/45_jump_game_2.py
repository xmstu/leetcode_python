# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    假设你总是可以到达数组的最后一个位置。

    每次看两步, 看第一步对应的第二步最远能去到那里, 第二步跳的最远的第一步就是要选取的
    """
    def jump(self, nums: List[int]) -> int:
        now = 0
        ans = 0
        while now < len(nums) - 1:
            right = now + nums[now]
            if right >= len(nums) - 1:
                return ans + 1
            nextRight = right
            the_next = now
            for i in range(now+1, right+1):
                print("i: %s, nums[i]: %s, nextRight: %s" % (i, nums[i], nextRight))
                if i + nums[i] > nextRight:
                    nextRight = i + nums[i]
                    the_next = i
            now = the_next
            ans += 1

        return ans


class Solution2:


    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        for i in range(1, n):
            j = 0
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[n-1]


class TestJump:
    """
    pytest -s 45_jump_game_2.py::TestJump
    """

    def test(self):
        solution = Solution2()

        nums = [2,3,1,1,4]
        assert 2 == solution.jump(nums)

        nums = [2,3,0,1,4]
        assert 2 == solution.jump(nums)
