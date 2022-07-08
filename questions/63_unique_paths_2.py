# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        递归, 自底向上, 从终点回溯将路径和加起来
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memory = dict()

        def isValid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and obstacleGrid[x][y] == 0
        
        def isEnd(x: int, y: int) -> bool:
            return x == m - 1 and y == n - 1
        
        def countPaths(x: int, y: int) -> int:
            # 已经在该点记录所有路径的点就直接返回, 记忆化搜索
            if (x, y) in memory:
                return memory[(x, y)]
            # 遇到障碍物或超出矩阵, 返回0
            if not isValid(x, y):
                return 0 
            # 到达终点, 返回 1 
            if isEnd(x, y):
                return 1
            # 在回溯的时候将路径数量加起来
            res = countPaths(x + 1, y) + countPaths(x, y + 1)
            memory[(x, y)] = res
            return res

        return countPaths(0, 0)
    

class Solution2:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        自顶向下, 从起点开始, 计算每个点的路径和, 到达终点停止
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                elif i == 0 and j == 0:
                    f[i][j] = 1
                elif i == 0:
                    f[i][j] = f[i][j - 1]
                elif j == 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[m - 1][n - 1]

class TestUniquePath:
    """
    pytest -s 63_unique_paths_2.py::TestUniquePath
    """

    def test(self):
        solution = Solution2()

        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        assert 2 == solution.uniquePathsWithObstacles(obstacleGrid)

        obstacleGrid = [[0,1],[0,0]]
        assert 1 == solution.uniquePathsWithObstacles(obstacleGrid)
