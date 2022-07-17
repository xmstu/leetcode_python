# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    以后再来理解
    """
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        f = [[[1e9] * (k + 1) for l in range(n)] for length in range(n)]
        for l in range(n):
            f[l][l][1] = 0
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                for i in range(2, k + 1):
                    for p in range(l, r):
                        f[l][r][i] = min(f[l][r][i], f[l][p][1] + f[p + 1][r][i - 1])
                sum = 0
                for p in range(l, r + 1):
                    sum += stones[p]
                f[l][r][1] = min(f[l][r][1], f[l][r][k] + sum)
        return f[0][n - 1][1] if f[0][n - 1][1] != 1e9 else -1


class TestMergeStones:

    """
    pytest -s 1000_minimum_cost_to_merge_stones.py::TestMergeStones
    """

    def test(self):
        solution = Solution()

        stones = [3,2,4,1]; K = 2
        assert 20 == solution.mergeStones(stones, K)

        stones = [3,2,4,1]; K = 3
        assert -1 == solution.mergeStones(stones, K)

        stones = [3,5,1,2,6]; K = 3
        assert 25 == solution.mergeStones(stones, K)
