# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
            if self.used[i] is False:
                # 排列放当前数字, 并标记使用过
                self.permutaion.append(nums[i])
                self.used[i] = True
                print("before recur petmutaion: %s, used: %s, i: %s, pos: %s" % (self.permutaion, self.used, i, pos))
                self.recur(nums, pos + 1)
                # 回到上一层, 还原现场 
                self.used[i] = False
                self.permutaion.pop()
                print("after recur petmutaion: %s, used: %s, i: %s, pos: %s" % (self.permutaion, self.used, i, pos))


class Solution2:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return []

        result = []
        self.dfs(nums, 0, result)
        return result

    def dfs(self, arr, depth, result):
        """
        举个简单的例子，
        假设我们有 [2, 5, 8, 9, 10][2,5,8,9,10] 这 55 个数要填入，
        已经填到第 33 个位置，已经填了 [8, 9][8,9] 两个数，
        那么这个数组目前为 [8, 9 | 2, 5, 10]这样的状态，分隔符区分了左右两个部分。
        假设这个位置我们要填 10 这个数，为了维护数组，我们将 2 和 10 交换，
        即能使得数组继续保持分隔符左边的数已经填过，右边的待填 [8, 9, 10 | 2, 5] 
        """
        if depth == len(arr):
            result.append(arr[:])
            return 

        for i in range(depth, len(arr)):
            arr[i], arr[depth] = arr[depth], arr[i]
            self.dfs(arr, depth + 1, result)
            arr[i], arr[depth] = arr[depth], arr[i]


class TestPermutations:

    """
    pytest -s 46_permutations.py::TestPermutations
    """

    def test(self):
        solution = Solution()

        nums = [1,2,3]
        assert [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] == solution.permute(nums)

        nums = [0,1]
        assert [[0,1], [1,0]] == solution.permute(nums)

        nums = [1]
        assert [[1]] == solution.permute(nums)

