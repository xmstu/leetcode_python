# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    你可以按 任何顺序 返回答案。

    这道题基本上和 78 题的做法一样, 组合是在子集的基础上进行剪枝
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.ans = []
        self.chosen = []
        # 从1开始计算
        self.recur(1)
        return self.ans

    def recur(self, i: int):
        # 组合需要剪枝, 【chosen的组合大于 k 个数字】 或 【当前的chosen的组合加上剩下的也不足k个】, 就没要继续递归了
        if len(self.chosen) > self.k or len(self.chosen) + (self.n - i + 1) < self.k:
            print("cut branch, chosen: %s, i: %s" % (self.chosen, i))
            return

        # 递归边界, 因为是从 1 开始计算, 所以递归边界是 n + 1
        if i == self.n + 1:
            # 因为 py 的列表是可变类型, 需要将中间结果深拷贝再append到最后的结果
            print("end recur chosen: %s, i: %s" % (self.chosen, i))
            self.ans.append(self.chosen[:])
            return
        
        # 每层要做的事, 选 i 或 不选 i

        # 不选 i
        self.recur(i + 1)

        # 选 i
        self.chosen.append(i)
        self.recur(i + 1)

        # 走完一层逻辑的时候, 回到上一层, 需要还原 chosen
        self.chosen.pop()


class TestCombinations:

    """
    pytest -s 77_combinations.py::TestCombinations
    """

    def test(self):
        solution = Solution()

        n, k = 4, 2
        assert [[3,4],[2,4],[2,3],[1,4],[1,3],[1,2]] == solution.combine(n, k)

        print()

        n, k = 1, 1
        assert [[1]] == solution.combine(n, k)

