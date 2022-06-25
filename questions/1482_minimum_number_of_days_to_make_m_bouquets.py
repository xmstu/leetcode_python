# -*- coding:utf-8 -*-
from typing import List



class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        latestBloomDay = 0
        for bloom in bloomDay:
            latestBloomDay = max(latestBloomDay, bloom)
        
        left, right = 0, latestBloomDay + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.validateOnDay(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        
        # 如果 right 等于最晚开花日期 + 1, 说明制作失败
        if right == latestBloomDay + 1:
            return -1
        return right
            

    def validateOnDay(self, bloomDay: List[int], m: int, k: int, now: int):
        # 花束数量
        bouquet = 0
        # 连续开花的数量
        consecutive = 0
        for bloom in bloomDay:
            if bloom <= now:
                consecutive += 1
                # 够了 k 朵花开花, 那么就可以制作一束花
                if consecutive == k:
                    bouquet += 1
                    consecutive = 0
            # 因为 bloom > now 还未开花, 连续开花数量清零
            else:
                consecutive = 0
        
        # 判断花束数量是否大于等于 要求的 m 束
        return bouquet >= m


class TestMinDays:

    """
    pytest -s 1482_minimum_number_of_days_to_make_m_bouquets.py::TestMinDays
    """

    def test(self):
        solution = Solution()

        bloomDay = [1,10,3,10,2]; m = 3; k = 1
        assert 3 == solution.minDays(bloomDay, m, k)

        bloomDay = [1,10,3,10,2]; m = 3; k = 2
        assert -1 == solution.minDays(bloomDay, m, k)

        bloomDay = [7,7,7,7,12,7,7]; m = 2; k = 3
        assert 12 == solution.minDays(bloomDay, m, k)
