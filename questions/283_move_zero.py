# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[n] = num
                n += 1
        while n < len(nums):
            nums[n] = 0
            n += 1
        return
 

class TestMoveZero(object):

    """
    执行命令跑单测:  pytest -s 283_move_zero.py::TestMoveZero
    """

    def test_move_zero(self):
        solution = Solution()
        nums = [0,1,0,3,12]
        solution.moveZeroes(nums)
        assert nums == [1,3,12,0,0]
        nums = [0]
        solution.moveZeroes(nums)
        assert nums == [0]

