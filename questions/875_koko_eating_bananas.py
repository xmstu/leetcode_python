# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left 是 香蕉堆的最小值, right 是香蕉堆的最大值
        left, right = min(1, min(piles)), max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return right
    
    def canFinish(self, piles: List[int], h: int, k: int):
        cost_hours = 0 
        for pile in piles:
            if pile < k:
                cost_hours += 1
            else:
                cost_hours += (pile - 1) // k + 1
        
        return cost_hours <= h


class TestMinEatingSpeed:

    """
    pytest -s 875_koko_eating_bananas.py::TestMinEatingSpeed
    """

    def test(self):

        solution = Solution()

        piles = [3,6,7,11]; h = 8
        assert 4 == solution.minEatingSpeed(piles, h)

        piles = [30,11,23,4,20]; h = 5
        assert 30 == solution.minEatingSpeed(piles, h)

        piles = [30,11,23,4,20]; h = 6
        assert 23 == solution.minEatingSpeed(piles, h)

        piles, h = [312884470], 968709470
        assert 1 == solution.minEatingSpeed(piles, h)
