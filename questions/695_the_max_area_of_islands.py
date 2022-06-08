# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-08-11
    :Copyright: (c) 2021, hexm
"""
from typing import List


class Solution(object):

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
            return 0
        # 用2标志为遍历过的陆地
        grid[r][c] = 2
        return 1 + self.dfs(grid, r - 1, c) + self.dfs(grid, r + 1, c) + self.dfs(grid, r, c - 1) + self.dfs(grid, r, c + 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        一个岛屿是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid 的四个边缘都被 0（代表水）包围着。
        找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

        示例1
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
        :param grid:
        :return:
        """
        nr, nc = len(grid), len(grid[0])
        res = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    res = max(self.dfs(grid, r, c), res)

        return res


class TestMaxAreaOfIslands(object):
    """
    执行命令跑单测:  pytest -s the_max_area_of_islands.py::TestMaxAreaOfIslands
    """

    def test_solution(self):
        solution = Solution()
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        max_area = solution.maxAreaOfIsland(grid)
        print("max area: %s" % max_area)
        assert 6 == max_area
