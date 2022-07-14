# -*- coding:utf-8 -*-
from typing import List


"""

"""


class Solution:

    """
    给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
    请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
    假设每一种面额的硬币有无限个。 
    题目数据保证结果符合 32 位带符号整数。


    该题是完全背包问题的模型题, 每钟面额硬币有无限个, 因此, 零钱等于物品, 体积等于面值, 价值等于1
    """

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.insert(0, 0)

        f = [0] * (amount + 1)
        f[0] = 1

        for i in range(1, n + 1):
            for j in range(coins[i], amount + 1):
                f[j] += f[j - coins[i]]
        
        return f[amount]


class TestCoinChange:

    """
    pytest -s 518_coin_change_2.py::TestCoinChange
    """

    def test(self):
        solution = Solution()

        amount = 5; coins = [1,2,5]
        assert 4 == solution.change(amount, coins)

        amount = 3; coins = [2]
        assert 0 == solution.change(amount, coins)

        amount = 10; coins = [10]
        assert 1 == solution.change(amount, coins)

