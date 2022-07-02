# -*- coding:utf-8 -*-
from collections import deque
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
        self.m = len(matrix)
        self.n = len(matrix[0])
        # 出边数组, 下标是出发点, 值是终点
        self.edges = [[] for _ in range(self.m * self.n)]
        # 入度数组, 入度为0就是最小的数或已经考虑过了
        self.deg = [0 for _ in range(self.m * self.n)]
        # 距离数组, 记录从出发点到自己当前最长的递增路径长度
        self.dist = [0 for _ in range(self.m * self.n)]
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        for i in range(self.m):
            for j in range(self.n):
                for k  in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if self.in_area(ni, nj) and matrix[i][j] < matrix[ni][nj]:
                        self.addEdge(self.num(i, j), self.num(ni, nj))
        
        self.topsort()
        ans = 0
        for i in range(self.m * self.n):
            ans = max(ans, self.dist[i])
        
        return ans
    
    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n
    
    def num(self, i: int, j: int):
        # 将二维下标转成一维数组的下标
        return i * self.n + j
    
    def addEdge(self, u: int, v: int):
        self.edges[u].append(v)
        self.deg[v] += 1
    
    def topsort(self):
        # 自顶向下, 计算最远的点
        q = deque()
        for i in range(self.m * self.n):
            if self.deg[i] == 0:
                q.appendleft(i)
                self.dist[i] = 1
        while q:
            x = q.pop()
            for y in self.edges[x]:
                self.deg[y] -= 1
                self.dist[y] = max(self.dist[y], self.dist[x] + 1)
                if self.deg[y] == 0:
                    q.appendleft(y)
   

class TestLongestIncreasingPath:

    """
    pytest -s 329_longest_increasing_path.py::TestLongestIncreasingPath
    """

    def test(self):
        solution = Solution2()

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
