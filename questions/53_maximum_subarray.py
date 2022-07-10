# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        我们用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」
        动态规划转移方程
            f(i) = max(f(i-1) + nums[i], nums[i])
        """
        # pre 记录了上一个连续子数组的最大和
        pre, ans = 0, nums[0]
        for num in nums:
            # 当上一个连续子数组的和加上当前数还小于当前数, 证明前面的数加起来是负收益, 新的连续子数组从当前数开始
            pre = max(pre + num, num)
            ans = max(ans, pre)
        return ans
    
    def maxSubArray2(self, nums: List[int]) -> int:
        pre = ans = nums[0]
        for num in nums[1:]:
            if pre > 0:
                pre += num
            else:
                pre = num
            ans = max(ans, pre)
        return ans
    
    def maxSubArray3(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        for index, num in enumerate(nums):
            # 边界条件: f[0] = ans = nums[0]
            if index == 0:
                f[index] = num
                ans = num
                continue
            f[index] = max(f[index - 1] + num, num)
            ans = max(ans, f[index])
        
        print("f: %s" % f)
        print("ans: %s" % ans)
        return ans


class TestMaxSubArray:

    """
    pytest -s 53_maximum_subarray.py::TestMaxSubArray
    """

    def test(self):
        solution = Solution()

        nums = [-2,1,-3,4,-1,2,1,-5,4]
        assert 6 == solution.maxSubArray3(nums)

        nums = [1]
        assert 1 == solution.maxSubArray3(nums)

        nums = [5,4,-1,7,8]
        assert 23 == solution.maxSubArray(nums)

        nums = [-2,1]
        assert 1 == solution.maxSubArray(nums)
