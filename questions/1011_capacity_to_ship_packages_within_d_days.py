# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.canSendAll(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        
        return right
    
    def canSendAll(self, weights: List[int], days: int, cap: int):
        cost_days = 1
        load = 0
        for weight in weights:
            if load + weight > cap:
                cost_days += 1
                load = 0
            load += weight
       
        return cost_days <= days
        


class TestShipWithinDays:

    """
    pytest -s 1011_capacity_to_ship_packages_within_d_days.py::TestShipWithinDays
    """

    def test(self):
        solution = Solution()

        weights = [1,2,3,4,5,6,7,8,9,10]; days = 5
        assert 15 == solution.shipWithinDays(weights, days)

        weights = [3,2,2,4,1,4]; days = 3
        assert 6 == solution.shipWithinDays(weights, days)

        weights = [1,2,3,1,1]; days = 4
        assert 3 == solution.shipWithinDays(weights, days)

        weights = [3,3,3,3,3,3]; days = 2
        assert 9 == solution.shipWithinDays(weights, days)
