# -*- coding:utf-8 -*-
from typing import List

class Solution:

    """
    给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_area(x, y):
            return 0 <= x < nrow and 0 <= y < ncol

        def dfs(x, y):
            # 递归边界
            if board[x][y] in ("X", "B"):
                return
            
            # 每层要做的事
            # 将和边界连通的改为 B
            board[x][y] = "B"
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not in_area(nx, ny):
                    continue
                dfs(nx, ny)

        # 从边界开始dfs
        for col in range(ncol):
            if board[0][col] == "O":
                dfs(0, col)
            if board[nrow - 1][col] == "O":
                dfs(nrow - 1, col)
        for row in range(nrow):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][ncol - 1] == "O":
                dfs(row, ncol - 1)
    
        
        # 遍历一遍矩阵, 将所有还是 O 的全部改为 X
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == "O":
                    board[row][col] = "X"
        

        # 遍历一遍矩阵, 将所有是 B 的全部还原为 O
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == "B":
                    board[row][col] = "O"


class TestSolve:

    """
    pytest -s 130_surrounded_regions.py::TestSolve
    """

    def test(self):

        solution = Solution()

        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]

        solution.solve(board)
        """
        被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
        任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
        如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
        """
        assert [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ] == board

        board = [["X"]]
        solution.solve(board)
        assert [["X"]] == board
