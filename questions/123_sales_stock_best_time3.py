# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:

    """
    给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        c = 2
        # 0. move index to 1-based
        prices.insert(0, 0)

        # 1. define f, initailize -∞
        f = [[[float("-inf")] * (c + 1) for _ in range(2)] for _ in range(n + 1)]
        f[0][0][0] = 0

        # 2. loop over all states
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(c + 1):
                    # 3. decisions
                    # 啥也不干, 休息
                    f[i][j][k] = f[i - 1][j][k]
                    # 卖出股票
                    if j == 0:
                        f[i][0][k] = max(f[i][0][k], f[i - 1][1][k] + prices[i])
                    # 买入股票
                    if j == 1 and k > 0:
                        f[i][1][k] = max(f[i][1][k], f[i - 1][0][k - 1] - prices[i])
                   
        
        print("f: %s" % f)
        # 4. return target
        ans = 0
        for k in range(c + 1):
            ans = max(ans, f[n][0][k])
        return ans


class TestSalesStockBestTime3(object):

    """
    pytest -s 123_sales_stock_best_time3.py::TestSalesStockBestTime3
    """

    def test_solution(self):
        solution = Solution()

        prices = [3,3,5,0,0,3,1,4]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 6

        prices = [1,2,3,4,5]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 4


