# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
    这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
    同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n in (1, 2):
            return max(nums)
        # 因为第一个房间和最后一个房间相邻, 形成环, 因此用两个dp数组, 一个从第一个房间开始dp, 一个从第二个房间开始
        # 最后看 两个 dp 数组最后一位哪个大

        # dp1 是 从nums的 0 到 n - 1
        dp1 = [0] * n 
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        # dp2 是 从nums的 1 到 n
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        # 因为盗窃不能盗窃相邻的房间, 因此 dp1[i - 2] + nums[i] 和 dp1[i-1] 比, 谁最大要谁
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            dp2[i + 1] = max(dp2[i - 1] + nums[i + 1], dp2[i])
        
        print("dp1: %s" % dp1)
        print("dp2: %s" % dp2)
        return max(dp1[n - 2], dp2[n - 1])


class TestRob:

    """
    pytest -s 213_house_robber_2.py::TestRob
    """

    def test(self):

        solution = Solution()

        """
        你不能先偷窃 1 号房屋(金额 = 2), 然后偷窃 3 号房屋(金额 = 2), 因为他们是相邻的。
        """
        nums = [2,3,2]
        assert 3 == solution.rob(nums)

        nums = [1,2,3,1]
        assert 4 == solution.rob(nums)

        nums = [1,2,3]
        assert 3 == solution.rob(nums)

