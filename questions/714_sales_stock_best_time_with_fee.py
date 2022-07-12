# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # 0. move index to 1-based
        prices.insert(0, 0)

        # 1. define f, initailize -∞
        f = [[float('-inf')] * 2 for _ in range(n + 1)]
        f[0][0] = 0

        # 2. loop over all states
        for i in range(1, n + 1):
            # 3. decisions
            # 买入股票
            f[i][1] = max(f[i][1], f[i - 1][0] - prices[i] - fee)
            # 卖出股票
            f[i][0] = max(f[i][0], f[i - 1][1] + prices[i])
            # 啥也不干, 休息
            for j in range(2):
                f[i][j] = max(f[i][j], f[i - 1][j])
        
        print("f: %s" % f)
        # 4. return target
        return f[n][0]


class TestSalesStockBestTimeWithFee(object):

    """
    pytest -s 714_sales_stock_best_time_with_fee.py::TestSalesStockBestTimeWithFee
    """

    def test_solution(self):
        solution = Solution()
        prices = [1, 3, 2, 8, 4, 9]; fee = 2

        """
        能够达到的最大利润:  
        在此处买入 prices[0] = 1
        在此处卖出 prices[3] = 8
        在此处买入 prices[4] = 4
        在此处卖出 prices[5] = 9
        总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
        """
        total_profit = solution.maxProfit(prices, fee)
        assert total_profit == 8

        prices = [1,3,7,5,10,3]; fee = 3
        total_profit = solution.maxProfit(prices, fee)
        assert total_profit == 6

