# -*- coding:utf-8 -*-
from typing import List



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = float("-inf")
        imax, imin = 1, 1
        for num in nums:
            if num < 0:
                imax,imin = imin,imax
            imax, imin = max(imax*num, num), min(imin*num, num)
            maxNum = max(maxNum, imax)
        return maxNum


class TestMaxProduct(object):


    def test_max_product(self):
        solution = Solution()
        nums = [2,3,-2,4]
        assert 6 == solution.maxProduct(nums)
        nums = [-2,0,-1]
        assert 0 == solution.maxProduct(nums)
        nums = [3,7,0,-1]
        assert 21 == solution.maxProduct(nums)

