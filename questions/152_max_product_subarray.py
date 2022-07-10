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
    
class Solution2:
    """
    给你一个整数数组 nums, 请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字）, 并返回该子数组所对应的乘积。
    测试用例的答案是一个 32-位 整数。
    子数组 是数组的连续子序列。

    思路, 利用动规数组求得最大乘积, 因为很大的负数乘以一个小的负数反而更大, 因此需要 fmax 和 fmin 两个动规数组求得最大乘积
    动规的方程:
        max 和 min 一起作为代表, 才满足最优子结构
        fmax[i], fmin[i] 表示以下标 i 为结尾的乘积最大, 最小数组
        fmax[i] = max(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
        fmin[i] = min(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
        最开始 fmax[0] = fmin[0] = nums[0]
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        fmax = [1] * n
        fmin = [1] * n
        fmax[0] = fmin[0] = ans = nums[0]
        for i in range(1, n):
            fmax[i] = max(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
            fmin[i] = min(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
            ans = max(ans, fmax[i])

        print("fmax: %s" % fmax)
        print("fmin: %s" % fmin)
        print("ans: %s" % ans)
        return ans


class TestMaxProduct(object):

    """
    pytest -s 152_max_product_subarray.py::TestMaxProduct
    """

    def test_max_product(self):
        solution = Solution2()
        nums = [2,3,-2,4]
        assert 6 == solution.maxProduct(nums)
        nums = [-2,0,-1]
        assert 0 == solution.maxProduct(nums)
        nums = [3,7,0,-1]
        assert 21 == solution.maxProduct(nums)

