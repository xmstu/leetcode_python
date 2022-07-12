# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:

    """
    给定一个整数数组prices, 其中第 prices[i] 表示第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 0. move index to 1-based
        prices.insert(0, 0)

        # 1. define f, initailize -∞
        f = [[[float("-inf")] * 2 for _ in range(2)] for _ in range(n + 1)]
        f[0][0][0] = 0

        # 2. loop over all states
        for i in range(1, n + 1):
            for j in range(2):
                for l in range(2):
                    # 3. decisions
                    # 买入股票, 买入之前没有冷冻期, 买入后也没有冷冻期
                    f[i][1][0] = max(f[i][1][0], f[i - 1][0][0] - prices[i])
                    # 卖出股票, 卖出进入冷冻期
                    f[i][0][1] = max(f[i][0][1], f[i - 1][1][0] + prices[i])
                    # 什么也不干, 状态转移过来, 随着时间推移, 冷冻期解除
                    f[i][j][0] = max(f[i][j][0], f[i - 1][j][l])
                   
        
        print("f: %s" % f)
        # 4. return target, 最大利润既可能出现在冷冻期，也可能出现在非冷冻期的状态
        return max(f[n][0][1], f[n][0][0])


class TestSalesStockBestTimeWithCooldown(object):

    """
    pytest -s 309_sales_stock_best_time_with_cooldown.py::TestSalesStockBestTimeWithCooldown
    """

    def test_solution(self):
        solution = Solution()
        prices = [1,2,3,0,2]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 3

        prices = [1]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 0

