# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    你是一个专业的小偷，计划偷窃沿街的房屋。
    每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # 记录初始状态, 第一个位置最大的就是房间0, 第二个是 0 或 1 中金额最大的那个
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # 因为盗窃不能盗窃相邻的房间, 因此 dp[i - 2] + nums[i] 和 dp[i-1] 比, 谁最大要谁
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[n - 1]


class Solution2:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 0)

        f = [[float("-inf")] * 2 for _ in range(n+1)]
        f[0][0] = 0

        for i in range(1, n+1):
            for _ in range(2):
                f[i][0] = max(f[i - 1][0], f[i - 1][1])
                f[i][1] = f[i - 1][0] + nums[i]
        
        return max(f[n][0], f[n][1])


class TestRob:

    """
    pytest -s 198_house_robber.py::TestRob
    """

    def test(self):

        solution = Solution()

        nums = [1,2,3,1]
        assert 4 == solution.rob(nums)

        nums = [2,7,9,3,1]
        assert 12 == solution.rob(nums)

