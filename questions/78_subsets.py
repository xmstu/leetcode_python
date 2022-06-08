# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.chosen = []
        self.recur(nums, 0)
        return self.ans

    def recur(self, nums: List[int], i: int):
        # 递归边界
        if i == len(nums):
            # 因为 py 的列表是可变类型, 需要将中间结果深拷贝再append到最后的结果
            self.ans.append(self.chosen[:])
            return
        
        # 每层要做的事, 选nums[i] 或 不选nums[i]

        # 不选 nums[i]
        self.recur(nums, i + 1)

        # 选nums[i]
        self.chosen.append(nums[i])
        self.recur(nums, i + 1)

        # 走完一层逻辑的时候, 回到上一层, 需要还原 chosen
        self.chosen.pop()


class TestSubsets:

    """
    pytest -s 78_subsets.py::TestSubsets
    """

    def test(self):
        solution = Solution()

        nums = [1,2,3]
        assert [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]] == solution.subsets(nums)

        nums = [0]
        assert [[], [0]] == solution.subsets(nums)
