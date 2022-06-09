# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nums排一下序, 保证剪枝判断不出错
        nums.sort()
        self.n = len(nums)
        # 中间结果, 每次排列的结果
        self.permutaion = []
        # 最终结果
        self.ans = []
        # 用一个数组记录数组里的每个数字是否有使用过 
        self.used = [False for _ in nums]
        self.recur(nums, 0)
        return self.ans

    def recur(self, nums: List[int], pos: int):
        # 递归边界
        if pos == self.n:
            self.ans.append(self.permutaion[:])
            return

        # 每层需要做的事情
        for i in range(self.n):
            if self.used[i] is True:
                continue
            # 剪枝
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] is False:
                continue
            # 排列放当前数字, 并标记使用过
            self.permutaion.append(nums[i])
            self.used[i] = True
            print("before recur petmutaion: %s, used: %s, i: %s, pos: %s" % (self.permutaion, self.used, i, pos))
            self.recur(nums, pos + 1)
            # 回到上一层, 还原现场 
            self.used[i] = False
            self.permutaion.pop()
            print("after recur petmutaion: %s, used: %s, i: %s, pos: %s" % (self.permutaion, self.used, i, pos))


class TestPemuteUnique:

    """
    pytest -s 47_permutations_2.py::TestPemuteUnique
    """

    def test(self):
        solution = Solution()

        assert [[1,1,2],[1,2,1],[2,1,1]] == solution.permuteUnique([1,1,2])

        assert [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == solution.permuteUnique([1,2,3])

        assert [[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]] == solution.permuteUnique([3,0,3,3])
