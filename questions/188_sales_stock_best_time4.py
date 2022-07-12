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

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        c = k
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


class TestSalesStockBestTime4(object):

    """
    pytest -s 188_sales_stock_best_time4.py::TestSalesStockBestTime4
    """

    def test_solution(self):
        solution = Solution()

        k = 2; prices = [2,4,1]
        total_profit = solution.maxProfit(k, prices)
        assert total_profit == 2

        """
        在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
        随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
        """
        k = 2; prices = [3,2,6,5,0,3]
        total_profit = solution.maxProfit(k, prices)
        assert total_profit == 7


