# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        示例 1:
        输入: prices = [7,1,5,3,6,4]
        输出: 7
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

        示例 2:
        输入: prices = [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

        示例 3:
        输入: prices = [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
        :param prices:
        :return:
        """
        min_price = float('inf')
        max_profit = 0
        total_profit = 0
        for index, price in enumerate(prices):
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
            # 只有当前的利润大于0, 并且当日价格高于明天的价格的时候才卖出，参考现实生活就是: 我知道明天股票会跌，那么今天我就卖出, 递增波段利润相加必然是最大利润
            if max_profit > 0 and index + 1 < len(prices) and price > prices[index + 1]:
                total_profit += max_profit
                max_profit = 0
                min_price = price
        # 连续上升的股票, 最后再卖出
        else:
            total_profit += max_profit
        return total_profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            # 亏了是负数, 最大值是0, 不用管, 大于0是赚了, 加到ans
            ans += max(prices[i] - prices[i-1], 0)
        
        return ans

class TestSalesStockBestTime2(object):

    """
    pytest -s sales_stock_best_time2.py::TestSalesStockBestTime2
    """

    def test_solution(self):
        solution = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 7

        prices = [1, 2, 3, 4, 5]
        total_profit = solution.maxProfit(prices)
        assert total_profit == 4

