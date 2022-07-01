# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    深度优先
    给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.dist = [[0] * self.n for _ in range(self.m)]
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        ans = 0
        for i in range(0, self.m):
            for j in range(0, self.n):
                ans = max(ans, self.dfs(i, j))
        
        return ans
    
    def dfs(self, x, y):
        # 自底向上递归, 递归到最远的点, 在返回的时候距离 + 1
        if self.dist[x][y] != 0:
            return self.dist[x][y]
        self.dist[x][y] = 1
        for k in range(0, 4):
            nx = x + self.dx[k]
            ny = y + self.dy[k]
            if self.in_area(nx, ny) and self.matrix[nx][ny] > self.matrix[x][y]:
                self.dist[x][y] = max(self.dist[x][y], self.dfs(nx, ny) + 1)
        return self.dist[x][y]

    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n



class Solution2:

    """
    广度优先
    给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pass


class TestLongestIncreasingPath:

    """
    pytest -s 329_longest_increasing_path.py::TestLongestIncreasingPath
    """

    def test(self):
        solution = Solution()

        matrix = [
            [9,9,4],
            [6,6,8],
            [2,1,1],
        ]
        # 最长递增路径为 [1, 2, 6, 9]。
        assert 4 == solution.longestIncreasingPath(matrix)

        matrix = [
            [3,4,5],
            [3,2,6],
            [2,2,1]
        ]
        # 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动
        assert 4 == solution.longestIncreasingPath(matrix)

        matrix = [[1]]
        assert 1 == solution.longestIncreasingPath(matrix)
