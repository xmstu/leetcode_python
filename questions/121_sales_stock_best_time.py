# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution:
    """
    买卖股票的最佳时机
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        获取买卖股票的最佳时机
        - 输入：[7,1,5,3,6,4]
        - 输出：5
        - 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
            注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

        1. 从上面的解释我们可以知道，数组的索引其实是日期，时间是只能向前流动的，因此只能低买高卖
        2. 解决这道题有两个要点，要记录: 历史最低价格 和 历史最大利润
        3. 在遍历价格数组的时候，不断比较当前价格和前一个价格，获取历史最低价格，每一天的价格减去历史最低价格得到当天的利润，更新历史最大利润
        :param prices:
        :return:
        """
        # 初始化历史最低价格
        min_price = float('inf')
        # 初始化历史最大利润
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit


class TestMaxProfit(object):
    """
    执行命令跑单测:  pytest -s sales_stock_best_time.py::TestMaxProfit
    """

    def test_solution(self):
        solution = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = solution.maxProfit(prices)
        print("max profit: %s" % max_profit)
        assert max_profit == 5

        prices = [7, 6, 4, 3, 1]
        max_profit = solution.maxProfit(prices)
        print("max profit: %s" % max_profit)
        assert max_profit == 0

        # 历史最高(5) - 历史次低(2) > 历史次高(3) - 历史最低(1)
        # 因为，利润是有两个值相减得到，因此，必须动态计算历史最大利润和历史最低点
        prices = [2, 5, 1, 3]
        max_profit = solution.maxProfit(prices)
        print("max profit: %s" % max_profit)
        assert max_profit == 3
