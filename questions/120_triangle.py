# -*- coding:utf-8 -*-
from typing import List



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp[i][j] 表示从点 (i, j) 到底边的最小路径和
        # 加多一行防止边界判断
        dp = [[0] * (n+1) for _ in range(n+1)]

        # 从三角形的最后一行开始递推
        for i in range(n - 1, -1, -1):
            for j in range(0, i+1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]


class TestMinimumTotal:

    """
    pytest -s 120_triangle.py::TestMinimumTotal
    """

    def test(self):
        solution = Solution()

        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        assert 11 == solution.minimumTotal(triangle)

        triangle = [[-10]]
        assert -10 == solution.minimumTotal(triangle)
