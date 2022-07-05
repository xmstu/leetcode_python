# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
    每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
    注意，一开始你手头没有任何零钱。
    给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true，否则返回 false。
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5: 0, 10: 0, 20: 0}

        def exchange(amount: int) -> bool:
            for x in [20, 10, 5]:
                while amount >= x and coins[x] > 0:
                    amount -= x
                    coins[x] -= 1
            return amount == 0

        for bill in bills:
            coins[bill] += 1
            amount = bill - 5
            if amount and not exchange(amount):
                return False
        return True


class TestLemonadeChange:

    """
    pytest -s 860_lemonade_change.py::TestLemonadeChange
    """

    def test(self):
        solution = Solution()

        bills = [5,5,5,10,20]
        assert True == solution.lemonadeChange(bills)

        bills = [5,5,10,10,20]
        assert False == solution.lemonadeChange(bills)
