# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    """
    def canPartition(self, nums: List[int]) -> bool:
        """
        思路
        1. 类 0/1 背包问题, 每个数选或不选, 其实也是子集问题;
        2. 两个子集相等, 就是每个子集的和等于总和的一半, 因此动规的时候算一个子集即可, 算该子集和是否等于总和一半;
        3. 总和是奇数的, 除以 2 必然有余数 1, 因此nums总和是奇数的不可能有两个子集元素和相等;
        """
        n = len(nums)
        nums.insert(0, 0)
        the_sum = sum(nums)
        if the_sum % 2 == 1:
            return False
        
        # 动规数组开一半即可
        f = [False] * (the_sum // 2 + 1)
        f[0] = True

        # f[i][j] 前 i 个数选出一些数, 总和是j, 是否可行
        # f[i][j] = f[i - 1][j - nums[i]] || f[i - 1][j]
        for i in range(1, n + 1):
            j = the_sum // 2
            while j >= nums[i]:
                f[j] |= f[j - nums[i]]
                j -= 1
        
        return f[the_sum // 2]



class TestCanPartition:

    """
    pytest -s 416_partition_equal_subset_sum.py::TestCanPartition
    """

    def test(self):
        solution = Solution()
        
        nums = [1,5,11,5]
        assert True == solution.canPartition(nums)

        nums = [1,2,3,5]
        assert False == solution.canPartition(nums)
