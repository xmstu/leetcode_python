# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-26
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        题解：https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
        - 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
        - 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
        - 你可以认为每种硬币的数量是无限的。
        示例 1：
            输入：coins = [1, 2, 5], amount = 11
            输出：3
            解释：11 = 5 + 5 + 1
        示例2：
            输入：coins = [2], amount = 3
            输出：-1
        示例3：
            输入：coins = [1], amount = 0
            输出：0
        示例 4：
            输入：coins = [1], amount = 1
            输出：1
        示例5：
            输入：coins = [1], amount = 2
            输出：2
        提示：
            1 <= coins.length <= 12
            1 <= coins[i] <= 231 - 1
            0 <= amount <= 104
        :param coins:
        :param amount:
        :return:
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                print("dp[%s]: %s" % (x, dp[x]))
        print("dp: %s" % dp)
        return dp[amount] if dp[amount] != float('inf') else -1


class Solution2:

    """
    - **最优子结构** = 状态 + 最优化目标 + 最优化目标之间具有递推关系
    - 原始状态：剩余金额，已用硬币枚数，目标：到达终点（0元）
    - 新状态：剩余金额，**最优化**目标：硬币枚数最少
    - 推导关系："兑换 n 元的最少硬币枚数" opt(n) = min(opt(n-1), opt(n-9), opt(n-10)) + 1
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 1e9
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        
        if dp[amount] >= inf:
            dp[amount] = -1
        
        return dp[amount]


class TestCoinChange(object):
    """
    执行命令跑单测:  pytest -s coin_change.py::TestCoinChange
    """

    def test_solution(self):
        solution = Solution()
        coins = [1, 2, 5]
        amount = 11
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 3

        coins = [2]
        amount = 3
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == -1

        coins = [1]
        amount = 0
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 0

        coins = [1]
        amount = 1
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 1

        coins = [1]
        amount = 2
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 2

        coins = [1, 3, 5]
        amount = 8
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 2

        coins = [1, 2, 5, 10]
        amount = 18
        min_coin_num = solution.coinChange(coins, amount)
        print("rs min_coin_num: %s" % min_coin_num)
        assert min_coin_num == 4
