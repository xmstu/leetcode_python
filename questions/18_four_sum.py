# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        l = 0
        for l in range(len(nums) - 3):
            # l 去重, 相同数值的已经考虑过
            if l > 0 and nums[l - 1] == nums[l]:
                continue
            three_sum = target - nums[l]
            for k in range(l+1, len(nums) - 2):
                # k 也要去重
                if k > l + 1 and nums[k] == nums[k - 1]:
                    continue
                i, j = k + 1, len(nums) -1
                while i < j:
                    s = nums[k] + nums[i] + nums[j]
                    if s < three_sum:
                        i += 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                    elif s > three_sum:
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                    else:
                        ans.append([nums[l], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
        return ans


class TestFourSum:

    """
    pytest -s 18_four_sum.py::TestFourSum
    """

    def test(self):
        solution = Solution()

        nums = [1,0,-1,0,-2,2]; target = 0
        assert [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] == solution.fourSum(nums, target)

        nums = [2,2,2,2,2]; target = 8
        assert [[2,2,2,2]] == solution.fourSum(nums, target)
